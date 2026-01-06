import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # activate api key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# Movie recommendation system
st.title("🍿🎥✮⋆˙Movie Recommendation System🍿🎥✮⋆˙")
user_input =st.text_input("Enter the movie name")
submit = st.button("Click here...")

#if submit and user_input.strip():
 #   st.markdown("Movie name has been entered")
#else: 
#    st.warning("Enter the movie name")

model=genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.markdown(f"Movie name entered:{user_input}")
    response=model.generate_content(f"Generate Movie Recommediation related to:{user_input}")
    st.write(f"Related Recomendation for similar movies: /n {response.text}")

else:
    st.write("You need to enter the movie name")