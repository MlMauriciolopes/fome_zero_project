# Libraries
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

#st.set_page_config(page_title='Countries', page_icon='🍽️', layout='wide')

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
st.header('🍽️ Visão Tipos de Cozinhas')
st.subheader('Melhores restaurantes dos principais tipos culinários')

# #logo
# image_path = r'C:\Users\mlsil\OneDrive\Documentos\repos\projeto_final_ftc\logo\logo.png'
# image = Image.open(image_path)
# st.sidebar.image(image, width=120)


# st.sidebar.markdown("""___""")

st.sidebar.markdown('# Filtros')
country_options = st.sidebar.multiselect(
    'Selecione os países das cidades que você deseja informações:',
    df.loc[:, "country"].unique().tolist(),
    default=['Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England'])

# Texto / função slider
st.sidebar.markdown('## Selecione a quantidade de restaurantes de sua preferência:  ')

top_slider = st.sidebar.slider(
    'Até qual valor ?',
    min_value = (0),
    max_value = (20),
    value = (10)
)

cuisines_options = st.sidebar.multiselect(
    'Tipos de culinárias: ',
    df.loc[:, "cuisines"].unique().tolist(),
    default=['Italian', 'Japanese', 'Chinese',
       'French', 'Fast Food', 'Indian'])


st.sidebar.markdown("""___""")
st.sidebar.markdown('### Powered by Maurício Lopes')

# # Filtro de restaurantes
# linhas_selecionadas = df['restaurant_id'] < date_slider
# df = df.loc[linhas_selecionadas, :]
# st.dataframe(df)

# # Filtro de países
# linhas_selecionadas = df['country'].isin(country_options)
# df = df.loc[linhas_selecionadas, :]
# #st.dataframe(df)

########################################################################
# Layout do Streamlit
########################################################################
with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # Restaurante italiano com a maior média de avaliação
        lines = (df['cuisines'] == 'Italian')
        cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']

        maior_media_culinaria_italiana = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().iloc[0,4]
        col1.metric(label='Italiana:Darshan', value='4.9/5.0')
        
    with col2:
        # REstaurante Americano com a melhor média de avaliação
        lines = (df['cuisines'] == 'American')
        cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']

        maior_media_culinaria_americana = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().iloc[0,4]
        col2.metric(label='Americana: Burger & Lobster', value= '4.9/5.0')
            
    with col3:
        # Restaurante árabe com a melhor média de avaliação
        lines = (df['cuisines'] == 'Arabian')
        cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']

        maior_media_culinaria_arabe = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().iloc[0,4]
        col3.metric(label='Arabe: Mandi@36', value= '4.7/5.0')
                
    with col4:
        # Restaurante japonês com a melhor média de avaliação
        lines = (df['cuisines'] == 'Japanese')
        cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']

        maior_media_culinaria_japonesa = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().iloc[0,4]
        col4.metric(label='Japonesa: Sushi Samba', value= '4.9/5.0')

    with col5:
        # Restaurante brasileiro com a melhor média de avaliação
        lines = (df['cuisines'] == 'Brazilian')
        cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']

        maior_media_culinaria_brasileira = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().iloc[0,4]
        col5.metric(label='Brasileira: Braseiro da Gávea', value= '4.9/5.0')
        #col5.metric('Brasileira: Braseiro da Gávea', {maior_media_culinaria_brasileira}, '/5.0')

with st.container():
    st.header(f'TOP {top_slider} restarantes')
    # Top restaurantes
    
    #cols
    cols = ['restaurant_id','restaurant_name','cuisines', 'aggregate_rating']
    
    # lines
    condition = (df['country'].isin(country_options)) & (df['cuisines'].isin(cuisines_options))
                                                          
    maior_media_culinaria_italiana = df.loc[condition, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).reset_index().head(top_slider)
    st.dataframe(maior_media_culinaria_italiana)
    
    

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'##### Top {top_slider} melhores tipos de culinárias ')
        # Top melhores tipos de culinárias
        maior_nota_media_culinaria = (df.loc[:, ['cuisines', 'aggregate_rating']].groupby(['cuisines']).mean()
                              .sort_values(['aggregate_rating'], ascending=[False]).reset_index().head(top_slider))

        # Barplot
        fig = px.bar(maior_nota_media_culinaria, x='cuisines', y='aggregate_rating', labels={'cuisines':'Culinárias', 'aggregate_rating':'Avaliações'})
        
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(f'##### Top {top_slider} piores tipos de culinárias ')
        # Top piores tipos de culinárias
        menor_nota_media_culinaria = (df.loc[:, ['cuisines', 'aggregate_rating']].groupby(['cuisines']).mean()
                              .sort_values(['aggregate_rating'], ascending=[True]).reset_index().head(top_slider))
        # Barplot
        fig = px.bar(menor_nota_media_culinaria, x='cuisines', y='aggregate_rating',
                     labels={'cuisines':'Culinárias', 'aggregate_rating':'Avaliações'})
        
        st.plotly_chart(fig, use_container_width=True)