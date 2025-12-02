# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os  # <- needed to handle file paths

# ---- Get the folder where this script is located ----
APP_PATH = os.path.dirname(__file__)

# ---- Load model ----
with open(os.path.join(APP_PATH, 'best_model_xgb.pkl'), 'rb') as file:
    model = pickle.load(file)

# ---- Load postal_mean ----
postal_mean = pd.read_pickle(os.path.join(APP_PATH, 'postal_mean.pkl'))

# ---- Preprocessor class ----
class Preprocessor:
    def __init__(self, postal_mean):
        self.postal_mean = postal_mean

    def transform(self, number_rooms, living_area, property_type, state, postal_code):
        df = pd.DataFrame({
            "number_rooms": [number_rooms],
            "living_area": [living_area],
            "property_type_name": [property_type],
            "state_mapped": [state],
            "postal_code": [str(postal_code)]
        })

        # Encode categorical features
        df['property_house'] = (df['property_type_name'] == 'house').astype(int)
        df['state_ready'] = (df['state_mapped'] == 'ready_to_move_in').astype(int)

        # Target encoding for postal code
        df['postal_code_target'] = df['postal_code'].map(self.postal_mean)
        df['postal_code_target'] = df['postal_code_target'].fillna(self.postal_mean.mean())

        return df[['number_rooms', 'living_area', 'property_house', 'state_ready', 'postal_code_target']]

# ---- Streamlit UI ----
st.title("House Price Predictor")

number_rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
living_area = st.number_input("Living Area (m²)", min_value=20, max_value=500, value=120)

property_type = st.selectbox("Property Type", ['house', 'apartment'])
state = st.selectbox("State of the Property", ['ready_to_move_in', 'under_construction'])

postal_code = st.text_input("Postal Code", "1000")

if st.button("Predict Price"):
    preprocessor = Preprocessor(postal_mean)
    input_data = preprocessor.transform(
        number_rooms, living_area, property_type, state, postal_code
    )

    # Model outputs log(price), convert to real price
    pred_log = model.predict(input_data)[0]
    pred_price = np.expm1(pred_log)

    st.success(f"🏡 Predicted Price: €{pred_price:,.0f}")
