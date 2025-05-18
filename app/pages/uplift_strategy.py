
import streamlit as st
import pandas as pd
import numpy as np

st.header("📈 Uplift Strategy Optimization")

st.markdown("Simulate targeting strategy under budget using uplift scores.")

n_customers = st.slider("Number of customers", 100, 10000, 1000)
budget = st.number_input("Marketing Budget ($)", value=10000)
cost_per_treatment = st.number_input("Cost per treatment ($)", value=10)

if st.button("Simulate"):
    simulated = pd.DataFrame({'customer_id': range(n_customers), 'uplift_score': np.random.rand(n_customers)})
    top = simulated.sort_values(by='uplift_score', ascending=False).head(int(budget // cost_per_treatment))
    st.write("Top customers to target:")
    st.dataframe(top.head(10))
