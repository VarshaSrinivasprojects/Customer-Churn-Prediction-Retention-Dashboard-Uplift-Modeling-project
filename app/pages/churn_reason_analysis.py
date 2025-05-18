import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("🧠 Churn Reason Analysis")

st.markdown("""
This page visualizes the predicted reasons behind customer churn.  
When a multi-class classifier is integrated, this section will use live model results.

The chart below uses simulated predictions for demo purposes.
""")

# Simulate churn reason predictions
np.random.seed(42)
reasons = ["Voluntary", "Contract End", "Upgrade/Migration"]
simulated_preds = np.random.choice(reasons, size=200, p=[0.6, 0.3, 0.1])
reason_df = pd.DataFrame(simulated_preds, columns=["ChurnReason"])

# Display value counts
reason_counts = reason_df.value_counts().reset_index()
reason_counts.columns = ["Churn Reason", "Count"]

st.bar_chart(reason_counts.set_index("Churn Reason"))

# Optional: Pie Chart
if st.checkbox("Show pie chart"):
    fig, ax = plt.subplots()
    ax.pie(reason_counts["Count"], labels=reason_counts["Churn Reason"], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

st.success("🔧 You can later replace `simulated_preds` with model.predict(X_new) from your multi-class churn model.")
