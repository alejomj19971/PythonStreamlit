import streamlit as st
import pandas as pd
import numpy as np



#Title sirve para mostrar un titulo con un texto como parámetro
st.title("Movilidad Incidentes 2022 - Medellín")

# se lee el archivo en data,queda en un formato de texto compatible para crear un dataframe
data = pd.read_csv('archivo.csv')
df = pd.DataFrame(data)

st.write(df)

# Renombramos las columnas latitud y longitud ,para que los datos puedan ser leidos por el componente map
df = df.rename(columns={'LATITUD': 'LAT'})
df = df.rename(columns={'LONGITUD': 'LON'})

# Se crean menus desplegables con el nombre mes y día se les pasa en las opciones unos filtros(més y día) del dataframe ordenado en orden ascendente, y sin elementos repetidos
month = st.selectbox('MES',(df["MES"].sort_values(ascending=True).unique()))  
day = st.selectbox('DÍA',(df["DIA"].sort_values(ascending=True).unique()))   
clase = st.selectbox('CLASE',(df["CLASE"].sort_values(ascending=True).unique()))  
comuna = st.selectbox('COMUNA',(df["COMUNA"].sort_values(ascending=True).unique()))  

# se coloca la fecha en un formato que permita la comparación
df['FECHA'] = pd.to_datetime(df['FECHA'])
filtro = (df['MES'] == month) & (df['DIA'] ==day) & (df['CLASE'] ==clase)& (df['COMUNA'] ==comuna)  

# Extraer columnas y filas del dataSet
df_filtrado = df.loc[filtro] 
df_filtrado = df_filtrado.loc[:, ['LAT', 'LON']]    

# se le pasa al mapa los datos
df = pd.DataFrame(
    df_filtrado,
    columns=['LAT', 'LON'])

# 
st.map(df)