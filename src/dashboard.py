import streamlit as st
import plotly.express as px
import pandas as pd

# Carregando a base de dados (substitua 'seu_arquivo.csv' pelo nome real do seu arquivo)
df = pd.read_csv('D:\\Documentos\\Portifolio\\anime_analysis\\src\\data\\imdb_anime_enhanced.csv')

# Configuração do título
st.title('Anime Dashboard')

# Filtros interativos
ano_filtro = st.slider('Filtrar por Ano:', int(df['Init_year'].min()), int(df['Init_year'].max()), (int(df['Init_year'].min()), int(df['Init_year'].max())))
genero_filtro = st.multiselect('Filtrar por Gênero:', ['Todos'] + list(df['Genre'].unique()), default=['Todos'])
ongoing_filtro = st.selectbox('Filtrar por Status de Andamento:', ['Todos', 'Sim', 'Não'])

# Aplicar filtros
df_filtrado = df[(df['Init_year'].between(ano_filtro[0], ano_filtro[1])) & 
                 (df['Genre'].isin(genero_filtro) if 'Todos' not in genero_filtro else True) & 
                 ((df['Ongoing'] == 'Yes') if ongoing_filtro == 'Sim' else (df['Ongoing'] == 'No') if ongoing_filtro == 'Não' else True)]

# Exibir tabela com os resultados
st.write('### Tabela de Animes')
st.dataframe(df_filtrado[['Title', 'Init_year', 'Genre', 'Ongoing']].style.set_table_styles([{
             'selector':'td',
             'props': [('max-width', '150px'), ('world-wrap', 'break-word')]}]), 
             use_container_width=True)

# Criar gráfico interativo usando Plotly
fig = px.scatter(df_filtrado, x='Init_year', y='User Rating', color='Genre', hover_data=['Title'], title='Gráfico de User Rating por Ano e Gênero')
st.plotly_chart(fig)
