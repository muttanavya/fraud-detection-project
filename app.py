import streamlit as st

st.title("Credit Card Fraud Detection")

st.write("Enter transaction details below")

amount = st.number_input("Transaction Amount")

if st.button("Predict"):
    if amount > 1000:
        st.error("Fraudulent Transaction")
    else:
        st.success("Legitimate Transaction")
