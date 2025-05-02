import streamlit as st
from PIL import Image

# Configurações iniciais
st.set_page_config(page_title="Data Cleaner App", layout="wide")
#logo = Image.open("assets/logo.png")
#st.sidebar.image(logo, use_column_width=True)
st.sidebar.title("🧭 Navegação")
st.sidebar.info("Use o menu lateral para navegar entre as etapas.")
st.title("🧹 Data Cleaner App")
st.markdown("Bem-vindo ao aplicativo de limpeza de dados! Use o menu ao lado para começar.")    
