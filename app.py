import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("../vehicles_us.csv")
df = df[df["price"] < 100000]  # Filtrar precios extremos

# --- Encabezado ---
st.title("Análisis de Vehículos en EE. UU.")

# --- Casilla de verificación para mostrar histograma ---
if st.checkbox("Mostrar histograma de precios por modelo", value=True):
    top_models = df["model"].value_counts().head(10).index
    df_top = df[df["model"].isin(top_models)]
    fig1 = px.histogram(df_top, x="price", color="model", nbins=40, barmode="group",
                        title="Distribución de precios por modelo (Top 10)")
    st.plotly_chart(fig1, use_container_width=True)

# --- Casilla de verificación para mostrar dispersión ---
if st.checkbox("Mostrar gráfico de dispersión Precio vs Kilometraje", value=True):
    fig2 = px.scatter(df, x="odometer", y="price", color="type",
                      opacity=0.5, title="Precio vs Kilometraje por tipo de vehículo",
                      labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig2, use_container_width=True)