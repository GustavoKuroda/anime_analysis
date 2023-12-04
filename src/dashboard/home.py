import streamlit as st

def home():
    st.write('# An analysis of Japanese Anime: An In-Depth IMDB Data Set.')
    st.write('### About the data set:')
    st.write('The data set provides a comprehensive view of various animations ' +
            'listed on IMDb that are categorized under the genre "Animation" ' +
            'and originate from Japan. It includes details such as the title, ' + 
            'genre, user rating, number of votes, runtime, year of release, ' +
            'summary, stars, certificate, metascore, gross earnings, episode ' +
            'flag, and episode title when applicable.')
    st.write('### This web app:')
    st.write('Gathers a table, presented at "Animes" page, with some ' +
            'relevant information such as Title, Genre, User Rating, ' +
            'Init Year, Gross and Ongoing. The "Graphics" page introduce ' +
            'some graphics to data visualization. At both pages the ' +
            'data can be filtered by key parameters.')
    st.write('### Data set reference:')
    st.write('https://www.kaggle.com/datasets/lorentzyeung/all-japanese-anime-titles-in-imdb')
