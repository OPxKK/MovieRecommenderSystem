import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
    
    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



st.title('Movie Recommender System')

movies_dict = pickle.load(open('movies_to_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl.pbz2','rb'))
movies = pd.DataFrame(movies_dict)

option = st.selectbox(
     'What Movies would you like to watch?',
     movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)


    


