import pickle
import streamlit as st
import requests
import numpy as np

st.title("Movir recomendation system")
movies_data = pickle.load(open("movie_data.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movies_tuple = tuple(movies_data["title"].values)
selected_movie = st.selectbox("Select a movie to watch",movies_tuple)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    recomendation_movies = []
    recomended_movie_poster = []
    index = movies_data[movies_data['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        recomendation_movies.append(movies_data.iloc[i[0]].title)
        poster = fetch_poster(movies_data.iloc[i[0]].movie_id)
        recomended_movie_poster.append(poster)
    return recomendation_movies ,recomended_movie_poster   

if st.button("recomend"):
    name,poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])
        
        