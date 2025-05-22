import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert to DataFrame if necessary
if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

# Your OMDb API key
load_dotenv()
OMDB_API_KEY = os.getenv("API_KEY")  

st.set_page_config(page_title="FY-LMI : The Movie Partner", page_icon="🎬", layout="centered")

# Custom CSS for background and styling
st.markdown("""
    <style>
        /* Background gradient or image */
        .stApp {
            background-image: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            background-size: cover;
            background-attachment: fixed;
        }

        /* Center content and style text */
        h1 {
            color: #ffffff;
            text-align: center;
            font-size: 3em;
            margin-top: 0.5em;
        }

        .css-1v3fvcr { 
            color: white;
        }

        .stSelectbox > div > div {
            background-color: #1c1c1c;
            color: white;
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
        }

        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }

        .stTextInput, .stSelectbox {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


# Title and logo
st.image(".\logo.jpg", width=100)
st.markdown("<h1 style='text-align: center; color: white;'>FY-LMI : The Movie Partner</h1>", unsafe_allow_html=True)

# Dropdown
selected_movie = st.selectbox("What movie is your favourite?", movies['title'].values)

# Fetch poster from OMDb
def fetch_poster(title):
    url = f"https://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['Poster'] if data.get('Poster') and data['Poster'] != 'N/A' else None

# Recommend
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    posters = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster = fetch_poster(title)
        recommended_movies.append(title)
        posters.append(poster)
    
    return recommended_movies, posters

# Button
if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    st.subheader("Top 5 Movie Recommendations:")
    cols = st.columns(5)
    for idx in range(5):
        with cols[idx]:
            st.text(names[idx])
            if posters[idx]:
                st.image(posters[idx])
            else:
                st.write("Poster not found")
