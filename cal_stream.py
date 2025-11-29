import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "integer cannot be divided by zero"

st.write(f"Result: {result}")
st.balloons()
