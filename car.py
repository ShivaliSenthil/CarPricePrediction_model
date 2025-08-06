import streamlit as st
import pandas as pd
import joblib

# Load the model and vectorizer
model = joblib.load("model5.pkl")  # Make sure your model filename matches
# You don't need vectorizer here if you are not using text input

st.title("Car Price Prediction App")

# Input fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
owner = st.selectbox("Owner", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
selling_price = st.number_input("Selling Price (in lakhs)", min_value=0.0, value=5.0)

# Encoding inputs manually (should match training)
seller_type_encoded = 1 if seller_type == 'Individual' else 0
transmission_encoded = 1 if transmission == 'Automatic' else 0
owner_encoded = {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 'Fourth & Above Owner': 3}[owner]
fuel_encoded = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}[fuel_type]

# Create input DataFrame
input_data = pd.DataFrame([[seller_type_encoded, kms_driven, selling_price, year, transmission_encoded, fuel_encoded, owner_encoded]],
                          columns=['Seller_Type', 'Kms_Drive', 'Selling_Price', 'Year', 'Transmission', 'Fuel_Type', 'Owner'])

# Prediction
if st.button("Predict Car Price"):
    predicted_price = model.predict(input_data)
    st.success(f"Predicted Price: ₹{predicted_price[0]:,.2f} lakhs")
