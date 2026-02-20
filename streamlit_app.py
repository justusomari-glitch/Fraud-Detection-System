import streamlit as st
import requests

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="",
    layout="centered"
)
st.title("Fraud Detection System")
st.header("Analyze transaction Behaviour and detect suspicious activity in real time")
st.divider()

device_type=['mobile','desktop']
payment_method=['card','mpesa','paypal']

form_values={
    "Transaction Amount": None,
    "Account age": None,
    "Transaction Hour": None,
    "Is Account International": None,
    "Transactions In the last Hour": None,
   "Transactions in the last 24hours": None,
    "Previous fraud flag": None,
    "Payment Method": None,
    "Device Type": None,
}

with st.form(key="fraud_predictions"):
    form_values['Transaction Amount']=st.number_input("Amount Transacted:",min_value=5)
    form_values['Transaction Hour']=st.number_input("Transaction Hour:",min_value=5)
    form_values['Account Age']=st.number_input("Account Age:",min_value=5)
    form_values['Transactions In the last Hour']=st.number_input("Number of transactions in the last hour:",min_value=1)
    form_values['Transactions In the last 24Hours']=st.number_input("Number of transactions in the last 24hours:",min_value=2)    
    form_values['Payment Method']=st.selectbox("Payment Methods:",payment_method)
    form_values['Device Type']=st.selectbox("Please select the device type:",device_type)
    form_values['Is Account International']=st.checkbox("Is the account International:")
    form_values['Previous fraud flag']=st.checkbox("Has the account been flagged for fraud before?:")
    st.divider()
    submit_button=st.form_submit_button(label="Evauate Transaction")
    if submit_button:
        input_data={
            'transaction_amount':form_values['Transaction Amount'],
            'account_age_days':form_values['Account Age'],
            'transactions_last_1h':form_values['Transactions In the last Hour'],
            'transactions_last_24h':form_values['Transactions In the last 24Hours'],
            'payment_method':form_values['Payment Method'],
            'device_type':form_values['Device Type'],
            'transaction_hour':form_values['Transaction Hour'],
            'is_international':form_values['Is Account International'],
            'previous_fraud_flag':form_values['Previous fraud flag']
              }
        url="https://fraud-detection-system-6jvs.onrender.com/predict"
        response=requests.post(url,json=input_data,timeout=30)
        
        result=(response.json())
        st.write(f"### Evaluation Result: {result["is_fraud"]}")
        st.write(f"### Probability: {result["fraud_probability"]*100}%")
st.write("Threshold in use")

        

        


