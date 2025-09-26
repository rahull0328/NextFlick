import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
print(API_KEY)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={API_KEY}&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path