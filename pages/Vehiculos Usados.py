import streamlit as st

import pandas as pd
import numpy as np
import altair as alt



#Title sirve para mostrar un titulo con un texto como parámetro
st.title("Automoviles Usados -Los más vendidos")

# se lee el archivo en data,queda en un formato de texto compatible para crear un dataframe
data = pd.read_excel('carros.xlsx')
df = pd.DataFrame(data)


st.write(df)


precio = st.selectbox('PRECIO MÍNIMO',(df["Price"].sort_values(ascending=True).unique()))
precio2 = st.selectbox('PRECIO MÁXIMO',(df["Price"].sort_values(ascending=True).unique()))
marca = st.selectbox('MARCA',(df["Make"].sort_values(ascending=True).unique()))  
puertas = st.selectbox('PUERTAS',(df["Doors"].sort_values(ascending=True).unique()))  
transmsion = st.selectbox('TRANSMISIÓN',(df["Transmission"].sort_values(ascending=True).unique()))  
año = st.selectbox('AÑO MÍNIMO',(df["Year"].sort_values(ascending=True).unique()))  
año2 = st.selectbox('AÑO MÁXIMO',(df["Year"].sort_values(ascending=True).unique()))
pasajeros = st.selectbox('PAASAJEROS',(df["Passengers"].sort_values(ascending=True).unique()))
color = st.selectbox('COLOR',(df["Exterior_Colour"].sort_values(ascending=True).unique()))



#Filtro de barras el loc devuelve un nuevo dataframe con los datos filtrados
filtroBarras = (df['Price'] >= precio) &(df['Price']<=precio2) & (df['Doors'] == puertas) &(df['Make'] == marca)   & (df['Transmission'] == transmsion)
df_filtrado = df.loc[filtroBarras] 
df_filtrado = df_filtrado.loc[:,['Price','Make']]    


st.title("Automoviles Usados Por Precio,Marca,Puertas y Transmisión" )

st.bar_chart(df_filtrado.set_index('Price'))


st.title("Automoviles Usados Por Precio y Año" )
 
filtroBarras2 = (df['Price'] >= precio) &(df['Price']<=precio2) & ((df['Year']>=año) & (df['Year']<=año2))
df_filtrado2 = df.loc[filtroBarras2] 
df_filtrado2 = df_filtrado2.loc[:,['Price','Year']]   

st.bar_chart(df_filtrado2.set_index('Year'))

st.title("Automoviles Usados Por Cantidad de Puertas y Color" )
 
filtroBarras3 = (df['Doors'] == puertas) &(df['Exterior_Colour']==color)
df_filtrado3 = df.loc[filtroBarras3] 
df_filtrado3 = df_filtrado3.loc[:,['Make','Price']]   

st.bar_chart(df_filtrado3.set_index('Price'))






