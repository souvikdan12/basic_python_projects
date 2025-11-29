import streamlit as st

st.title("Basic Unit Converter Dashboard")
options = [
    "Kilometer to Meter",
    
    "Fahrenheit to Celsius",
   
    "Dollar to INR",
  
    "Gram to Kilogram",
    
]
choice = st.selectbox("Select a conversion type:", options)
rate = 83.0


if choice == "Kilometer to Meter": 
    km = st.number_input("Enter value in Kilometers:")
    if st.button("Convert"):
        m = km * 1000
        st.success(f"{km} Kilometers = {m} Meters")

elif choice == "Fahrenheit to Celsius":
    f = st.number_input("Enter value in Fahrenheit:")
    if st.button("Convert"):
        c = (f - 32) * 5/9
        st.success(f"{f} °F = {c:.2f} °C")

elif choice == "Dollar to INR":
    usd = st.number_input("Enter value in USD:" )
    if st.button("Convert"):
        inr = usd * rate
        st.success(f"{usd} USD = {inr:.2f} INR   (rate: {rate})")

elif choice == "Gram to Kilogram":
    g = st.number_input("Enter value in Grams:")
    if st.button("Convert"):
        kg = g / 1000
        st.success(f"{g} Grams = {kg} Kilograms")
