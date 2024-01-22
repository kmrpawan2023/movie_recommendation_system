import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movie_posters = []
    for j in movies_list:
        # movie_id = movies.iloc[j[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[j[0]].title)
        # recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
