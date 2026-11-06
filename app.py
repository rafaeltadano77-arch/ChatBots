import streamlit as st #biblioteca para criar a interface web
import pandas as pd #biblioteca para leitura e manipulação de dados
import json #biblioteca para trabalhar com arquivos JSON


#im
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

#Configuração do Streamlit(pagina web)
st.set_page_config(
    page_title=" chatbot Operadora Cartão ", #titulo da aba
    page_icon= "  💳 ", #Icone da aba
    layout= " centered " # centraliza o conteudo

)

#exibe o titulo principal da aplicação
st.title( "  chatbot atendimento - operadora de cartão " )
