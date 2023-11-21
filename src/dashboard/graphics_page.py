import streamlit as st
import plotly.express as px
import pandas as pd

def graphics_page():
    # Loading dataset
    df = pd.read_csv(f'src/data/imdb_anime_enhanced.csv')

    # Title
    st.title('Graphics')

    # Interactive filters
    year_filter = st.slider('Filter by Year:', int(df['Init_year'].min()), int(df['Init_year'].max()), (int(df['Init_year'].min()), int(df['Init_year'].max())))
    genre_filter = st.multiselect('Filter by Genre:', ['All'] + list(df['Genre'].unique()), default=['All'])
    ongoing_filter = st.selectbox('Filter by Ongoing:', ['All', 'Yes', 'No'])

    # Apply filters
    df_filtered = df[(df['Init_year'].between(year_filter[0], year_filter[1])) & 
                    (df['Genre'].isin(genre_filter) if 'All' not in genre_filter else True) & 
                    ((df['Ongoing'] == 'Yes') if ongoing_filter == 'Yes' else (df['Ongoing'] == 'No') if ongoing_filter == 'No' else True)]

    # Creating graphics using Plotly
    fig_scatter = px.scatter(df_filtered, x='Init_year', 
                    y='User Rating', color='Genre', 
                    hover_data=['Title'], 
                    title='User rating by Init_year and Genre Scatter.')

    fig_histogram = px.histogram(df_filtered, x='User Rating', 
                    nbins=int(1 + 10 * (df_filtered['User Rating'].max() - df_filtered['User Rating'].min())),
                    color='Init_year',
                    marginal='histogram',
                    title='User Rating by Init_year Histogram.',
                    labels={'User Rating': 'User Rating', 'Init_year': 'Init_year'})

    # Render graphics
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig_scatter, use_container_width=True)
    col2.plotly_chart(fig_histogram, use_container_width=True)
