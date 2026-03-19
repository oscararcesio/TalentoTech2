import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="centered", page_title="Talento Tech", page_icon=":bar_chart:")

# st.title("Análisis de datos con Python")
# st.markdown("Hola Mundo")


#creamos columnas
t1, t2 = st.columns([0.4,0.6])

t1.image('images.png')
t2.title("Análisis de datos con Python")
t2.markdown("**Oscar Arcesio** | email: **arcesio.cardenas@udea.edu.co**")

#crear pestañas

steps=st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña $\sqrt{9}$" ])

with steps[0] : 
    st.write("Contenido de la pestaña 1")

with steps[1]:
    st.title("Pestaña 2")

with steps[2]:
    df=pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4,5,6],
        'C': [7,8,9]
    })
    st.dataframe(df)

    fig, ax =plt.subplots()
    ax=sns.barplot(x=['A', 'B', 'C'], y=[1, 2, 3], ax=ax)
    ax.bar_label()
    st.pyplot(fig)

    # Abrimos streamlit.io para publicar las visualizaciones, funciona como un hosting
    # Luego creamos un repositorio público en GitHub y subimos el miercoles18.py y la imagen usada en el .py

