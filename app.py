import streamlit as st
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Initialize Flask app
flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mood_music.db'  # Update if using a different database
db = SQLAlchemy(flask_app)

# Function to initialize the database
def init_db():
    with flask_app.app_context():
        db.create_all()

init_db()

# Streamlit UI
st.title("AI Mood-Based Music Recommender")
st.write("Welcome to the Mood-Based Music Recommender!")

# Add your Streamlit UI components here...
