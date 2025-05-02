import streamlit as st
from src.loader import load_file
import pandas as pd

st.title("🔎 Visualizar Dados")

uploaded_file = st.file_uploader("Faça upload de um arquivo CSV ou Excel", type=["csv", "xlsx"])
if uploaded_file:
    df = load_file(uploaded_file)
    st.session_state["df_raw"] = df  # Salva no estado global
    st.subheader("Visualização")
    st.dataframe(df, use_container_width=True)

    st.subheader("Resumo Estatístico")
    st.write(df.describe(include="all"))
