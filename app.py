from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import streamlit as st

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mood_music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mood = db.Column(db.String(50), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()

# Initialize the database
init_db()

# Streamlit UI
def main():
    st.title("AI Mood-Based Music Recommender")
    name = st.text_input("Enter your name:")
    mood = st.selectbox("Select your mood:", ["Happy", "Sad", "Energetic", "Calm"])
    
    if st.button("Save Mood"):
        new_user = User(name=name, mood=mood)
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
        st.success(f"Mood saved for {name}!")

if __name__ == "__main__":
    main()
