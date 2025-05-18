
import streamlit as st
import pandas as pd

st.header("💰 LTV Estimation Dashboard")

st.markdown("Estimate Lifetime Value of customers based on their tenure and charges.")

monthly = st.number_input("Monthly Charges", value=70.0)
tenure = st.number_input("Tenure (Months)", value=12)

if st.button("Estimate LTV"):
    ltv = monthly * tenure
    st.metric("Estimated LTV", f"${ltv:.2f}")
