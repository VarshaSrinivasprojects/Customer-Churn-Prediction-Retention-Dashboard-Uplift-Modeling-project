import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.header("🔁 Churn Prediction Dashboard")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("models/saved_models.pkl")

model = load_model()

# Simulated user input form
st.subheader("📋 Enter Customer Details:")
with st.form("predict_form"):
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    Tenure = st.number_input("Tenure (Months)", min_value=0, value=12)
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

    submitted = st.form_submit_button("Predict Churn")

    if submitted:
        # Dummy encoding for Contract (as an example)
        contract_map = {
            "Month-to-month": [1, 0, 0],
            "One year": [0, 1, 0],
            "Two year": [0, 0, 1]
        }
        contract_features = contract_map[Contract]

        # Final feature vector
        features = [MonthlyCharges, Tenure] + contract_features
        input_df = pd.DataFrame([features], columns=[
            "MonthlyCharges", "tenure", "Contract_Month-to-month",
            "Contract_One year", "Contract_Two year"
        ])

        # Make prediction
        prediction = model.predict(input_df)[0]
        churn_prob = model.predict_proba(input_df)[0][1]

        st.metric("📊 Prediction", "Churn" if prediction == 1 else "No Churn")
        st.progress(float(churn_prob), text=f"Churn Probability: {churn_prob:.2%}")

