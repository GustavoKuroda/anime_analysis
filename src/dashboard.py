from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(f'D:\\Documentos\\Portifolio\\anime_analysis\\src\\data\\imdb_anime_enhanced.csv')

hist = px.histogram(df, 
                    x='User Rating', 
                    nbins=int(1 + 10 * (df['User Rating'].max() - df['User Rating'].min())),
                    color='Init_year',
                    color_discrete_sequence=px.colors.sequential.Reds,
                    marginal='histogram',
                    title='Distribution of User Rating.')
hist.update_layout(showlegend=False)
hist.update_traces(showlegend=False)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Anime', style={'textAlign':'center'}),
    dcc.Graph(figure=hist)
])

if __name__ == '__main__':
    app.run(debug=True)