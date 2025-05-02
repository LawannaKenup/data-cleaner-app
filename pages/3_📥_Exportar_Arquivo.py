import streamlit as st
from src.exporter import get_download_link

st.title("📥 Exportar Arquivo Limpo")

if "df_cleaned" not in st.session_state:
    st.warning("⚠️ Nenhum dataset limpo encontrado. Limpe os dados primeiro.")
else:
    df = st.session_state["df_cleaned"]
    st.markdown("Clique abaixo para exportar:")
    st.markdown(get_download_link(df), unsafe_allow_html=True)
