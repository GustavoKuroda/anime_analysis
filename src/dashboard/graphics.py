import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def graphics():
    # Loading dataset
    df = pd.read_csv(f'src/data/imdb_anime_enhanced.csv')

    # Title
    st.title('Graphics')

    # Interactive filters
    year_filter = st.slider('Filter by Year:', int(df['Init'].min()), int(df['Init'].max()), (int(df['Init'].min()), int(df['Init'].max())))
    genre_filter = st.multiselect('Filter by Genre:', ['All'] + list(df['Genre'].unique()), default=['All'])
    ongoing_filter = st.selectbox('Filter by Ongoing:', ['All', 'Yes', 'No'])

    # Apply filters
    df_filtered = df[(df['Init'].between(year_filter[0], year_filter[1])) & 
                    (df['Genre'].isin(genre_filter) if 'All' not in genre_filter else True) & 
                    ((df['Ongoing'] == 'Yes') if ongoing_filter == 'Yes' else (df['Ongoing'] == 'No') if ongoing_filter == 'No' else True)]
    
    # Calculate total gross and mean rating, with filtered dataframe
    total_gross = df_filtered['Gross'].sum()
    mean_rating = df_filtered['User Rating'].mean()

    # Calculate mean and standard deviation of User Rating for each year, without filtered dataframe
    mean_std_data = df.groupby('Init')['User Rating'].agg(['mean', 'std']).reset_index()

    # Creating graphics using Plotly
    hist1 = px.histogram(df_filtered, x='User Rating', 
                    nbins=int(1 + 10 * (df_filtered['User Rating'].max() - df_filtered['User Rating'].min())),
                    color='Init',
                    title='User Rating by Initial Year Histogram.',
                    labels={'User Rating': 'User Rating', 'Init': 'Init Year'})

    hist2 = px.histogram(df_filtered, x='Init',
                        nbins=70,
                        color='User Rating',
                        title='Animes released over the years.',
                        labels={'User Rating': 'User Rating', 'Init': 'Init Year'})
    
    time_series = px.line(mean_std_data, x='Init', y='mean', title='User Rating evolution.',
                        labels={'Init': 'Init Year', 'User Rating': 'User Rating'},
                        line_shape='linear', markers=True)

    # Adding error bars to time_series
    for index, row in mean_std_data.iterrows():
        year = row['Init']
        mean_value = row['mean']
        std_value = row['std']

        time_series.add_traces(go.Scatter(x=[year], y=[mean_value],
                        mode='markers',
                        error_y=dict(type='data', array=[std_value], visible=True),
                        marker=dict(color='red'),
                        showlegend=False))
    
    # Indicators
    ind1 = go.Figure()
    ind1.add_trace(
        go.Indicator(
            mode='number',
            value=total_gross,
            title='Total earnings',
            number={'prefix': 'US$'}
        )
    )

    ind2 = go.Figure()
    ind2.add_trace(
        go.Indicator(
            mode='number',
            value=mean_rating,
            title='Mean User Rating',
        )
    )

    # Render indicators
    col1, col2 = st.columns(2)
    col1.plotly_chart(ind1, use_container_width=True)
    col2.plotly_chart(ind2, use_container_width=True)

    # Render graphics
    st.plotly_chart(hist1, use_container_width=True)
    st.plotly_chart(hist2, use_container_width=True)
    st.plotly_chart(time_series, use_container_width=True)
