# bibliotecas necessárias
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

#st.set_page_config(page_title='Countries', page_icon='🏙️', layout='wide')

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
st.header('🏙️ Visão Cidades')

country_options = st.sidebar.multiselect(
    'Selecione AQUI os países das cidades que você deseja visualizar as informações:',
    df.loc[:, "country"].unique().tolist(),
    default=['Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England'])

st.sidebar.markdown("""___""")
st.sidebar.markdown('### Powered by Maurício Lopes')

########################################################################
# Layout do Streamlit
########################################################################
#Tabela 1
with st.container():    
    #st.markdown('# Visão Países')

    st.markdown('### Top 10 restaurantes registrados na base de dados')
    # Top restaurantes registrados na base de dados.
    
    # lines
    condition = (df['country'].isin(country_options))
    
    #cols
    cols = ['country', 'restaurant_id', 'city', 'color_name', 'rating_color']
    
    restaurantes_registrados = df.loc[condition, cols].groupby(['city']).count().sort_values(['restaurant_id'], ascending=False).reset_index().head(10)

    # Barplot
    fig = px.bar(restaurantes_registrados, x='city', y='restaurant_id', color='city', text_auto=True, labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes'})

    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('##### Top restaurantes com a média de avaliação acima de 4 estrelas')
        # Top restaurantes com a média de avaliação acima de 4 estrelas
        
        # lines / rating condition & condition
        rating_condition_mais = (df['aggregate_rating'] >= 4) & condition
        
        nota_acima_de_quatro = (df.loc[rating_condition_mais, ['restaurant_id', 'city']].groupby(['city']).count().sort_values(['restaurant_id'], ascending=False).reset_index()).head(10)

        # Barplot
        fig = px.bar(nota_acima_de_quatro, x='city', y='restaurant_id', color='city', text_auto='True', labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('##### Top restaurantes com média de avaliação abaixo de 2.5')
        # Top restaurantes com média de avaliação abaixo de 2.5
        
        # lines / rating condition & condition
        rating_condition_menos = (df['aggregate_rating'] <=2.5) & condition
        
        nota_abaixo_de_dois_e_meio = (df.loc[rating_condition_menos, ['restaurant_id', 'city']].groupby(['city']).count().sort_values(['restaurant_id'], ascending=False).reset_index()).head(10)

        # Barplot
        fig = px.bar(nota_abaixo_de_dois_e_meio, x='city', y='restaurant_id', color='city', text_auto=True,
                     labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes'})
        
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown('##### Top 10 cidades com restaurantes com tipos de culinárias distintas')
    # Top cidades com restaurantes com tipos de culinárias distintas
    culinarias_distintas = df.loc[condition, ['cuisines', 'city']].groupby(['city']).nunique().sort_values(['cuisines'], ascending=False).reset_index().head(10)

    # Barplot
    fig = px.bar(culinarias_distintas, x='city', y='cuisines', color='city', text_auto=True,
                 labels={'city':'Cidades', 'cuisines':'Quantidade de tipos de culinárias únicos'})
    
    st.plotly_chart(fig, use_container_width=True)
