import streamlit as st
import plotly.express as px
import pandas as pd

def animes():
    # Loading dataset
    df = pd.read_csv(f'src/data/imdb_anime_enhanced.csv')

    # Title
    st.title('Table')

    # Interactive filters
    year_filter = st.slider('Filter by Year:', int(df['Init_year'].min()), int(df['Init_year'].max()), (int(df['Init_year'].min()), int(df['Init_year'].max())))
    genre_filter = st.multiselect('Filter by Genre:', ['All'] + list(df['Genre'].unique()), default=['All'])
    ongoing_filter = st.selectbox('Filter by Ongoing:', ['All', 'Yes', 'No'])

    # Apply filters
    df_filtered = df[(df['Init_year'].between(year_filter[0], year_filter[1])) & 
                    (df['Genre'].isin(genre_filter) if 'All' not in genre_filter else True) & 
                    ((df['Ongoing'] == 'Yes') if ongoing_filter == 'Yes' else (df['Ongoing'] == 'No') if ongoing_filter == 'No' else True)]

    # Show results as a table
    st.write('### Animes table')
    st.dataframe(df_filtered[['Title', 'Genre', 'User Rating', 'Init_year', 'Gross', 'Ongoing']].style.set_table_styles([{
                'selector':'td',
                'props': [('max-width', '150px'), ('word-wrap', 'break-word')]}]), 
                use_container_width=True)
