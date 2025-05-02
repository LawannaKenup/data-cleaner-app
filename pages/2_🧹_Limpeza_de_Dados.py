import streamlit as st
from src.cleaner import remove_columns, drop_na_rows, fill_na_values, convert_columns

st.title("🧹 Limpeza de Dados")

# Verifica se o dataset foi carregado na sessão anterior
if "df_raw" not in st.session_state:
    st.warning("🚨 Primeiro envie um arquivo na aba 'Visualizar Dados'.")
else:
    df = st.session_state["df_raw"].copy()

    st.subheader("🔻 Remover Colunas")
    cols_to_remove = st.multiselect("Selecione colunas:", df.columns)
    if cols_to_remove:
        df = remove_columns(df, cols_to_remove)
        st.success(f"Removidas {len(cols_to_remove)} colunas.")

    st.subheader("💧 Valores Nulos")
    if st.checkbox("Remover linhas com valores nulos"):
        df = drop_na_rows(df)
        st.success("Linhas com valores nulos removidas.")

    if st.checkbox("Preencher valores nulos com valor específico"):
        val = st.text_input("Digite o valor para preenchimento:")
        if val:
            try:
                # Tenta converter o valor para float, se for possível
                val = float(val)
            except ValueError:
                pass  # Permite que o valor seja uma string, se não for possível converter para número
            df = fill_na_values(df, val)
            st.success(f"Valores nulos preenchidos com: {val}")

    st.subheader("🔁 Conversão de Tipos")
    cols_to_convert = st.multiselect("Colunas para conversão:", df.columns)
    convert_to = st.selectbox("Converter para:", ["int", "float", "str"])
    if st.button("Converter"):
        df = convert_columns(df, cols_to_convert, convert_to)
        st.success("Conversão realizada.")

        # Exibe os tipos de dados das colunas após a conversão
        st.write("Tipos de dados das colunas após conversão:")
        st.write(df.dtypes)

    # Armazena o DataFrame limpo no session state
    st.session_state["df_cleaned"] = df

    # Exibe uma prévia do DataFrame limpo
    st.subheader("📊 Prévia do Dataset Limpo")
    st.dataframe(df, use_container_width=True)
