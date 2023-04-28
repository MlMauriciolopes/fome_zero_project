import streamlit as st
from PIL import Image

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
import inflection

from haversine import haversine
from streamlit_folium import folium_static

from matplotlib import pyplot as plt
from matplotlib import gridspec
from folium.plugins import MarkerCluster

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


st.set_page_config(
    page_title="Home",
    page_icon="📊"
)

image = Image.open('logo.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown("# Fome Zero!")
    
# ########################################################################
# # Layout do Streamlit
# ########################################################################
with st.container():
    st.markdown("# Fome Zero!")
    st.markdown("## O melhor lugar para encontrar seu mais novo restaurante favorito!")
    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")
    
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        restaurantes_unicos = len(df['restaurant_name'].unique())
        col1.metric('Restaurantes cadastrados: ', restaurantes_unicos)
        
    with col2:
        paises_unicos = len(df['country'].unique())
        col2.metric('Países cadastrados: ', paises_unicos)
        
    with col3:
        cidades_unicas = len(df['city'].unique())
        col3.metric('Cidades cadastradas: ', cidades_unicas)
                
    with col4:
        avaliacoes = df.loc[:, 'votes'].sum()
        col4.metric('Avaliações feitas: ', avaliacoes)

    with col5:
        tipos_culinaria = len(df['cuisines'].unique())
        col5.metric('Tipos de culinárias : ', tipos_culinaria)

tab1, tab2 = st.tabs(['Visão Geral', 'Visão Geográfica'])

with tab1:
    with st.container():
        st.write("# Curry Company Growth Dashboard")
        st.markdown(
    """
    
    ### Como utilizar esse Dashboard do Fome Zero ?
    - Página Home:
        - Visão Geral: Informações gerais de comportamento.
        - Visão Geográfica: Insights de geolocalização.
        
    - Página countries: 
        - Quantidade de restaurantes, cidades, avaliações, e média de preços de pratos.
    - Página cities:
        - Mostra os TOP restaurantes, e as melhores e menores avaliações.
    - Página cuisines:
        - Visão Geral: Informações gerais de comportamento.
        - Mostra os restaurantes com as melhores colocações, seguindo a avaliação dos clientes.
    ### Ask for Help
    - Time de Data Science
    -  2023 - Maurício Lopes
    """
)

with tab2:
    with st.container():
        houses = df[['restaurant_name', 'latitude', 'longitude', 'aggregate_rating', 'city']].copy()
        
        map = folium.Map()

        for index, location_info in houses.iterrows():
          folium.Marker([location_info['latitude'],
                         location_info['longitude']],
                         popup=location_info[['restaurant_name','city', 'aggregate_rating']]).add_to(map)

        folium_static(map, width=1024, height=600)
