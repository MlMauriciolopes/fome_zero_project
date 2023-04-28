##################################################################################
# Libraries
##################################################################################
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
import streamlit as st
import inflection

from haversine import haversine
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title='Countries', page_icon='🌍', layout='wide')

# importando dataset
df1 = pd.read_csv('dataset/zomato.csv')

# Cópia do dataframe original
df = df1.copy()

##################################################################################
# Variaveis de ajuda / Help variables
##################################################################################
# Preenchimento dos nomes dos países / fill in country columns
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

# Criação do nome das Cores / Color column creation
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

###############################################################################
# Funções de ajuda / Help functions
###############################################################################

# Renomear as colunas do DataFrame / Rename dataframe columns
def rename_columns(dataframe):
  df = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  snakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(snakecase, cols_old))
  df.columns = cols_new

  return df

def country_name(country_id):
  return COUNTRIES[country_id]

def color_name(color_code):
  return COLORS[color_code]

df = rename_columns(df)
df.head(1)

# Criação do Tipo de Categoria de 'comida' / Creation of category type 'food'
def create_price_tye(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"

# # Renomeando as colunas do dataframe / Rename dataframe columns
# def adjust_columns_order(dataframe):
#     df = dataframe.copy()

#     new_cols_order = [
#         "restaurant_id",
#         "restaurant_name",
#         "country",
#         "city",
#         "address",
#         "locality",
#         "locality_verbose",
#         "longitude",
#         "latitude",
#         "cuisines",
#         "price_type",
#         "average_cost_for_two",
#         "currency",
#         "has_table_booking",
#         "has_online_delivery",
#         "is_delivering_now",
#         "aggregate_rating",
#         "rating_color",
#         "color_name",
#         "rating_text",
#         "votes",
#     ]

#     return df.loc[:, new_cols_order]

#########################################################################
# Limpeza do dataset / Dataset cleaning
#########################################################################

# Drop Valores 'NaN' do dataframe / Drop 'NaN' values in dataframe
df = df.dropna()

# Ajustando as colunas "price_range", "country_code", "rating_color", "cuisines" / Adjusting the columns "price_range", "country_code", "rating_color", "cuisines"
df['cuisines'] = df.loc[:, 'cuisines'].astype(str).apply(lambda x: x.split(",")[0])

df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x)) # Função CDS Discord

df["price_type"] = df.loc[:, "price_range"].apply(lambda x: create_price_tye(x)) # Função CDS Discord

df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x)) # Função CDS Discord

#====================================================================================
# BARRA LATERAL
#====================================================================================

# Textão
st.header('🌍 Visão Países')

st.sidebar.markdown('### Filtros')

country_options = st.sidebar.multiselect(
    'Escolha aqui os países que você deseja visualizar: ',
    df.loc[:, "country"].unique().tolist(),
    default=['Philippines', 'Brazil', 'Australia', 'United States of America', 'England', 'India'])

st.sidebar.markdown("""___""")
st.sidebar.markdown('### Powered by Maurício Lopes')

########################################################################
# Layout do Streamlit
########################################################################
#Tabela 1
with st.container():    
    #st.markdown('# Visão Países')

    st.markdown('### Quantidade de restaurantes registrados por país')
    # Quantidade de restaurantes registrados por país.
    
    # Lines
    condition = (df['country'].isin(country_options))
    
    restaurantes_registrados = df.loc[condition, ['restaurant_id', 'country']].groupby(['country']).count().sort_values(['restaurant_id'], ascending=False).reset_index()
    # Barplot
    fig = px.bar(restaurantes_registrados, x='country', y='restaurant_id', labels={'country':'Países', 'restaurant_id':'Quantidade de Restaurantes'})
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown('## Quantidade de cidades registradas por país')
    # Quantidade de cidades registradas por país
    cidades_registradas = df.loc[condition, ['city', 'country']].groupby(['country']).count().sort_values(['city'], ascending=False).reset_index()

    # Barplot
    fig = px.bar(cidades_registradas, x='country', y='city', labels={'country':'Países', 'city':'Cidades'})
    st.plotly_chart(fig, use_container_width=True)
        
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('##### Média de avaliações feitas por país')
        # Média de avaliações feitas por país
        maior_avaliacao_media = df.loc[condition, ['votes', 'country']].groupby(['country']).mean().sort_values(['votes'], ascending=False).reset_index()

        # Barplot
        fig = px.bar(maior_avaliacao_media, x='country', y='votes', labels={'country':'Países', 'votes':'Quantidade de Avaliações'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('##### Preço médio de um prato para duas pessoas')
        # Preço médio de um prato para duas pessoas
        prato_para_dois_media = df.loc[condition, ['average_cost_for_two', 'country']].groupby(['country']).mean().sort_values(['average_cost_for_two'], ascending=False).reset_index()

        # Barplot
        fig = px.bar(prato_para_dois_media, x='country', y='average_cost_for_two', labels={'country':'Países', 'average_cost_for_two':'Preço para duas pessoas'})
        st.plotly_chart(fig, use_container_width=True)
        
