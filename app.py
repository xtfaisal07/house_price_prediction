import streamlit as st
import numpy as np
import pickle

# Load the model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏡 House Price Prediction App")
st.write("Enter the details below to predict the house price (in 100,000s):")

# Input fields
med_inc = st.number_input("Median Income (in lacs)", min_value=0.0, max_value=20.0, value=5.0)
house_age = st.slider("House Age (in years)", 1, 100, 20)
ave_rooms = st.number_input("Average Number of Rooms", min_value=1.0, max_value=50.0, value=5.0)
ave_occup = st.number_input("Average Occupancy", min_value=1.0, max_value=10.0, value=2.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[med_inc, house_age, ave_rooms, ave_occup]])
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹{prediction[0]*100000:,.2f}")
