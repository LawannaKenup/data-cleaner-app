import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Análise", layout="wide")
st.title("📊 Dashboard Interativo de Análise de Dados")

# Verifica se há um DataFrame carregado na sessão
if "df_raw" in st.session_state:
    df = st.session_state["df_raw"]

    st.subheader("🔎 Pré-visualização")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Gráficos Interativos")
    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox("Selecione o eixo X", df.columns)
        y_axis = st.selectbox("Selecione o eixo Y", df.columns, index=min(1, len(df.columns) - 1))
        chart_type = st.radio("Tipo de gráfico", ["Scatter", "Bar", "Box"])

        try:
            if chart_type == "Scatter":
                fig = px.scatter(df, x=x_axis, y=y_axis, color=x_axis)
            elif chart_type == "Bar":
                fig = px.bar(df, x=x_axis, y=y_axis)
            else:
                fig = px.box(df, x=x_axis, y=y_axis)

            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Erro ao gerar o gráfico: {e}")

    with col2:
        st.subheader("📊 Distribuição de Coluna")
        dist_col = st.selectbox("Coluna para distribuição", df.columns)
        try:
            dist_fig = px.histogram(df, x=dist_col, nbins=30, title=f"Distribuição de {dist_col}")
            st.plotly_chart(dist_fig, use_container_width=True)
        except Exception as e:
            st.error(f"Erro ao gerar o histograma: {e}")

    st.markdown("---")

    st.subheader("📌 Correlações")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) >= 2:
        try:
            corr_df = df[numeric_cols].corr()
            corr_fig = px.imshow(corr_df, text_auto=True, aspect="auto", title="Matriz de Correlação")
            st.plotly_chart(corr_fig, use_container_width=True)
        except Exception as e:
            st.error(f"Erro ao calcular correlações: {e}")
    else:
        st.info("Poucas colunas numéricas para mostrar a correlação.")
else:
    st.warning("⚠️ Nenhum arquivo foi carregado ainda. Volte à primeira aba 'Visualizar Dados' para carregar um arquivo.")
