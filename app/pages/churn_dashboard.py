
import streamlit as st
import pandas as pd

st.header("🔁 Churn Prediction Dashboard")

st.markdown("Upload customer data or use simulated inputs to get churn predictions.")

# Simulate form input
with st.form("predict_form"):
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
    Tenure = st.number_input("Tenure (Months)", min_value=0)
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    submitted = st.form_submit_button("Predict Churn")
    if submitted:
        st.success("Prediction logic would be shown here (model integration pending)")
