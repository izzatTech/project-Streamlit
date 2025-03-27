import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria for password strength
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):  # Uppercase letter
        strength += 1
    if re.search(r"[a-z]", password):  # Lowercase letter
        strength += 1
    if re.search(r"\d", password):  # Digit
        strength += 1
    if re.search(r"[@$!%*?&]", password):  # Special character
        strength += 1

    # Strength levels
    if strength == 0:
        remarks = "Very Weak ❌"
        color = "red"
    elif strength == 1 or strength == 2:
        remarks = "Weak ⚠"
        color = "orange"
    elif strength == 3 or strength == 4:
        remarks = "Medium 🔵"
        color = "blue"
    else:
        remarks = "Strong ✅"
        color = "green"

    return strength, remarks, color

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.subheader("Check if your password is strong enough!")

# User input
password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks, color = check_password_strength(password)
    st.markdown(f"*Strength Level:* <span style='color:{color}; font-size:18px;'>{remarks}</span>", unsafe_allow_html=True)
    
    # Recommendations
    st.subheader("🔹 How to Improve Your Password:")
    if strength < 3:
        st.warning("✔ Use at least *8 characters*")
        st.warning("✔ Include *uppercase & lowercase* letters")
        st.warning("✔ Add *numbers and special characters*")

st.sidebar.header("🛡 Password Security Tips")
st.sidebar.write("🔑 Use a mix of uppercase, lowercase, numbers & special characters.")
st.sidebar.write("🔑 Avoid common passwords like '123456', 'password', or 'qwerty'.")
st.sidebar.write("🔑 Use a *password manager* to store strong passwords securely.")