import streamlit as st
import pickle
import pandas as pd

with open ("models/arima_model.pkl","rb") as f:
    model = pickle.load(f)
    
st.title("Arima model Forecasting") 
st.subheader("Air quality in Nairobi")
st.markdown("### ⚠️ Note")
st.write("This model was trained using data from the last quarter of 2017. and will start predictions from 12-12-2017 at 18:00")
st.image("nairobi.jpg", width=500)

st.title("Arima Forecasting app")
st.write("Please enter for how many periods you want to ***forecast*** the air quality and the start time")
n_steps = st.number_input("Periods", min_value=1, max_value=50, value=10)
if st.button("Forecast"):
    forecast = model.forecast(steps=n_steps)
    st.write(forecast)

    





   