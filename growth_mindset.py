import streamlit as st
import random

# List of Growth Mindset Quotes
growth_quotes = [
    "Your abilities can be developed through dedication and hard work.",
    "Failure is simply the opportunity to begin again, this time more intelligently.",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Effort and persistence lead to success.",
    "The only limit to your growth is the one you set in your mind."
]

# Streamlit App Layout
st.title("🚀 Growth Mindset Coach")
st.subheader("Boost your motivation and set goals!")

# Display a random motivational quote
if st.button("Get a Random Motivation 💡"):
    st.success(random.choice(growth_quotes))

# User Input: Personal Growth Reflection
st.subheader("📌 Set Your Growth Goals")
goal = st.text_area("What is one skill or habit you want to improve?", "")

if st.button("Save My Goal ✍"):
    if goal:
        st.success(f"Great! Stay focused on improving: *{goal}*")
    else:
        st.warning("Please enter a goal to stay motivated!")

# Extra Growth Mindset Tips
st.sidebar.header("📌 Growth Mindset Tips")
st.sidebar.write("💡 Challenges help you grow!")
st.sidebar.write("💡 Learn from your mistakes and improve!")
st.sidebar.write("💡 Keep pushing forward, no matter what!")

st.sidebar.markdown("---")
st.sidebar.write("📢 This app helps you build a strong Growth Mindset with motivation and goal-setting.")