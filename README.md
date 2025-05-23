
# Customer Churn Prediction + Retention Dashboard + Uplift Modeling

This end-to-end project predicts customer churn, estimates LTV, identifies top segments via uplift modeling, and enables business-driven decision-making through a Streamlit dashboard.

---

## 📦 Features

- 🔁 Churn prediction using a trained RandomForestClassifier
- 💰 LTV estimation by customer and segment
- 🧠 Multi-class churn reason simulation
- 📈 Uplift modeling using CausalML
- 🎯 Budget-optimized marketing simulator
- 📊 Interactive dashboard (Streamlit Cloud)

---

## 🧠 Model Training Details

- **Algorithm**: RandomForestClassifier
- **Input Features**: MonthlyCharges, tenure, Contract (one-hot)
- **Evaluation**: 80/20 train/test split
- **Accuracy**: ~80% on Telco dataset (light preprocessing)
- **Model Path**: `models/saved_models.pkl`

---

## 🖼️ Model Explanation

To enhance interpretability, adding:

```python
import shap
explainer = shap.Explainer(model.named_steps['classifier'])
shap_values = explainer(model.named_steps['preprocessor'].transform(X))
shap.plots.beeswarm(shap_values)
```


---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app/app.py
```

---

## 🚀 Deployed to Streamlit Cloud

---

## 📎 Live Demo

👉 https://customer-churn-prediction-retention-dashboard-uplift-modeling.streamlit.app/

---

## 👩‍💻 Author

Varsha Srinivas  
[LinkedIn](https://www.linkedin.com/in/varsha-srinivas-24011995) | [GitHub](https://github.com/VarshaSrinivasprojects)
