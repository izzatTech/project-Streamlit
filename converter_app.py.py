import streamlit as st 
st.set_page_config(page_title="Inch to Cm Converter", layout="centered")
st.title("Inch to Cm Converter")

inch = st.text_input("Enter Length in inches:")

if inch:
    try:
        inch = float(inch)  # Ensure inch is a float
        cm = inch * 2.54  # Convert inches to cm
        st.write(f"{inch} inches = {cm:.2f} cm**")  # Display result
    except ValueError:
        st.error("Please enter a valid number!")  # Error message for invalid input       