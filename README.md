
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

To enhance interpretability, consider adding:

```python
import shap
explainer = shap.Explainer(model.named_steps['classifier'])
shap_values = explainer(model.named_steps['preprocessor'].transform(X))
shap.plots.beeswarm(shap_values)
```

You can include this inside a Streamlit page later (e.g., `shap_dashboard.py`).

---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app/app.py
```

---

## 🚀 Deploy to Streamlit Cloud

1. Go to https://streamlit.io/cloud
2. Click **“New app”**
3. Connect your GitHub repo
4. Set:
   - **Branch**: `main`
   - **Main file path**: `app/app.py`
5. Click **Deploy**

---

## 📎 Live Demo

👉 Add your deployed Streamlit Cloud link here once available

---

## 👩‍💻 Author

Varsha Srinivas  
[LinkedIn](https://www.linkedin.com/in/varsha-srinivas-24011995) | [GitHub](https://github.com/VarshaSrinivasprojects)
