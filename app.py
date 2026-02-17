import pandas as pd
from pydantic import BaseModel
import joblib
from fastapi import FastAPI

app=FastAPI()
bundle=joblib.load("fraud_pipeline.pkl")
model=bundle["model"]
threshold=bundle["threshold"]

print("loaded threshold:",threshold)
print("loaded model:",type(model))

print(model.feature_names_in_)




@app.get("/")
def home():
    return{"message:","The API is on"}

class FraudData(BaseModel):
    account_age_days: int
    transaction_anount: float
    transaction_hour: int
    is_international: int
    transaction_last_1h: int
    transaction_last_24h: int
    previous_fraud_flag: int
    payment_method: str
    device_type: str

@app.host("/predict/Fraud Activity")
def predict_fraud_activity (data:FraudData):
    input_dic=data.model_dump
    input_df=pd.DataFrame([input_dic])
    proba=model.predict_proba(input_df)[0][1]
    prediction=int(proba>=threshold)

    if prediction==1:
        status="Fraudulent Transaction"
    else:
        status="Legitimate Transaction"

    return{
        "fraud_probability": float(proba),
        "threshold": threshold,
        "is_fraud": status
    }







