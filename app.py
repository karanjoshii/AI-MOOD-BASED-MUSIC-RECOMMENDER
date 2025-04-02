import streamlit as st
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize Flask app
flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mood_music.db'  
db = SQLAlchemy(flask_app)

# Function to initialize the database
def init_db():
    with flask_app.app_context():
        db.create_all()

init_db()

# Streamlit UI
st.title("AI Mood-Based Music Recommender 🎵")
st.write("Welcome to the Mood-Based Music Recommender!")

# Example button to test UI
if st.button("Start Recommendation"):
    st.write("Fetching music based on your mood...")

