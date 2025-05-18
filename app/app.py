
import streamlit as st

st.set_page_config(
    page_title="Customer Retention Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Customer Churn & Retention Strategy Dashboard")

st.markdown("""
Welcome to the end-to-end churn prediction, LTV modeling, and uplift optimization dashboard.

**Navigate using the sidebar** to explore:
- 🔁 Churn Prediction
- 💰 LTV Estimation
- 📈 Uplift Strategy
- 🧠 Churn Reason Analysis
""")

st.info("👈 Use the sidebar to get started.")
