import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Load the data
df = pd.read_csv(f'D:\\Documentos\\Portifolio\\anime_analysis\\src\\data\\imdb_anime_enhanced.csv')

# Starting Dash app
app = dash.Dash(__name__)

# App Loadout
app.layout = html.Div(children=[
    html.H1(children='Anime Dashboard'),

    # Interactive filters
    html.Label('Year Production Filter:'),
    dcc.RangeSlider(
        id='year-production-slider',
        min=df['Init_year'].min(),
        max=df['Init_year'].max(),
        step=1,
        marks={str(i): str(i) for i in range(df['Init_year'].min(), df['Init_year'].max() + 1)},
        value=[df['Init_year'].min(), df['Init_year'].max()]
    ),

    html.Label('User Rating Filter:'),
    dcc.RangeSlider(
        id='user-rating-slider',
        min=df['User Rating'].min(),
        max=df['User Rating'].max(),
        step=0.1,
        marks={i: str(i) for i in range(int(df['User Rating'].min()), int(df['User Rating'].max()) + 1)},
        value=[df['User Rating'].min(), df['User Rating'].max()]
    ),

    dcc.Dropdown(
        id='genre-dropdown',
        options=[{'label': genre, 'value': genre} for genre in df['Genre'].unique()],
        value=[],
        multi=True,
        placeholder='Genre'
    ),

    # Result table
    html.Table(id='result-table'),

])


# Update the table with the filters
@app.callback(
    Output('result-table', 'children'),
    [Input('year-production-slider', 'value'),
     Input('user-rating-slider', 'value'),
     Input('genre-dropdown', 'value')]
)
def update_table(year_production_range, user_rating_range, selected_genre):
    # Apply filters
    filtered_df = df[
        (df['Init_year'] >= year_production_range[0]) & (df['Init_year'] <= year_production_range[1]) &
        (df['User Rating'] >= user_rating_range[0]) & (df['User Rating'] <= user_rating_range[1]) &
        (df['Genre'].isin(selected_genre) if selected_genre else True)
    ]

    # Create HTML table
    table_rows = [html.Tr([html.Th(col) for col in filtered_df.columns])] + [
        html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns]) for i in range(len(filtered_df))
    ]

    return table_rows


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)