import streamlit as st 
st.title ("positive / negative number checker")
n = st.number_input("enter a number")
if n >=0 :
    st.success(f"{n} is a positive number")
else:
    st.error(f"{n} is a negative number")