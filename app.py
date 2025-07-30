import pandas as pd
import streamlit as st
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# crear grafico de dispersion
scat_button = st.button('Construir diagrama de dispersion')

if scat_button:  # al hacer clic en el boton
    st.write('Diagrama de dispersion de datos de anunciosde venta de coches')
    # crear diagrama de dispersion
    diag = px.scatter(car_data, x="odometer")
    st.plotly_chart(diag, use_container_width=True)
