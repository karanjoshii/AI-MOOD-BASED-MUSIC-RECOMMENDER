import streamlit as st
import pandas as pd
import numpy as np
import requests

# Title
st.title("AI Mood-Based Music Recommender")

# User Input: Mood Selection
mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Energetic", "Calm"])

# Placeholder function for music recommendations
def get_music_recommendations(mood):
    music_dict = {
        "Happy": ["Happy Song 1", "Happy Song 2", "Happy Song 3"],
        "Sad": ["Sad Song 1", "Sad Song 2", "Sad Song 3"],
        "Energetic": ["Energetic Song 1", "Energetic Song 2", "Energetic Song 3"],
        "Calm": ["Calm Song 1", "Calm Song 2", "Calm Song 3"]
    }
    return music_dict.get(mood, [])

# Display Recommendations
if st.button("Get Recommendations"):
    recommendations = get_music_recommendations(mood)
    st.write("### Recommended Songs:")
    for song in recommendations:
        st.write(f"- {song}")
