import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt 
# gravando o excel em uma variaveldf 
df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# titulo do Dashboard 
st.header("Meu Dashboard versao 2.0")
menu = st.tabs(["Tabela", "Barra", "Pizza"])
with menu[0]:
    st.dataframe(df)#expondo o df no dashboard
with menu [1]:
    # # grafico de barras vertical 
    fig = plt.figure(figsize=(10,6)) # tamanho do grafico
    sn.countplot(data=df, x= "setor",
                 order=df['setor'].value_counts().index,
                 palette='viridis')
    plt.title("Grafico de Barras por setor")
    plt.xlabel("Numero de empresas")
    plt.ylabel("Setor")
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(fig)
with menu [2]:
    # # grafico de pizza
    setor = df["setor"].value_counts()
    cores = sn.color_palette("Blues_r", len(setor)) # paleta degrade profissional
    fig = plt.figure(figsize= (10,6)) #tamanho do grafico
    plt.pie(setor,
            labels=setor.index,
            # autopct= '%1.1f%%',
            startangle=140,
            colors=cores,
            pctdistance=0.85, # afasta a porcentagem do centro
            wedgeprops={'linewidth': 3, 'edgecolor': 'white'})
    plt.show()
    st.pyplot(fig)