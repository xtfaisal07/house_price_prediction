
# 🏡 House Price Prediction Web App

This is a simple Machine Learning web application built with **Streamlit** that predicts house prices based on user input features. It uses the **California Housing Dataset** and a trained **Linear Regression** model.


## 🌐 Live Demo

> 🔗 https://housepricepredictx.streamlit.app/

> 🔗 You can deploy this app for free using [Streamlit Cloud](https://streamlit.io/cloud)


## 🚀 Features

- 📈 Predict house prices using trained ML model
- 🔢 Input features interactively via sliders and number inputs
- 📊 Real-time predictions on the frontend
- 📉 Visualize prediction output using Streamlit components

## 📁 Project Structure

```
house_price_streamlit_app/
│
├── app.py                 # Streamlit frontend
├── train_model.py         # Trains and saves the ML model
├── house_price_model.pkl  # Trained machine learning model
├── requirements.txt       # Dependencies
└── .gitignore             # Files/folders to ignore in Git
```

## 🧠 ML Model

- **Dataset**: California Housing Dataset (via `sklearn.datasets`)
- **Model**: Linear Regression
- **Target Variable**: Median House Value

## 💻 How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/xtfaisal07/house_price_prediction.git
cd house_price_prediction
```

2. **Set up virtual environment** (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Train the model** (if `house_price_model.pkl` doesn't exist):

```bash
python train_model.py
```

5. **Run the app**:

```bash
streamlit run app.py
```

## 📦 Requirements

- Python 3.8+
- Streamlit
- scikit-learn
- pandas
- numpy

## 📜 License

This project is licensed under the MIT License.

---

### ✨ Screenshots

<img width="1440" alt="Screenshot 2025-07-06 at 1 55 36 PM" src="https://github.com/user-attachments/assets/a924e398-cc09-4d7f-a45b-02e04c461038" />
<img width="1440" alt="Screenshot 2025-07-06 at 1 55 21 PM" src="https://github.com/user-attachments/assets/3856a542-49d6-46e2-a291-a68986344f3e" />




---

## 🙌 Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
