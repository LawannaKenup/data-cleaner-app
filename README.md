# 🧼📊 Data Cleaner & Analyzer

Uma aplicação web interativa desenvolvida com [Streamlit](https://streamlit.io/) para **limpeza, visualização e análise de dados** em arquivos `.csv` ou `.xlsx`. Ideal para profissionais de dados, estudantes ou qualquer pessoa que precise explorar datasets rapidamente sem escrever código.

---

## 🚀 Funcionalidades

🔹 **Upload de Arquivos**  
- Suporte a arquivos CSV e Excel (`.csv`, `.xlsx`)
- Visualização inicial das 10 primeiras linhas

🔹 **Limpeza de Dados**  
- Visualização e tratamento de valores ausentes
- Conversão de tipos
- Exclusão de colunas ou linhas

🔹 **Visualização Interativa**  
- Gráficos dinâmicos com Plotly (scatter, barras, boxplot)
- Histogramas de distribuição
- Matriz de correlação

🔹 **Exportação**  
- Download do dataset limpo em CSV


---

## ⚙️ Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/data-cleaner-dashboard.git
cd data-cleaner-dashboard
```

2. **Crie e ative um ambiente virtual (opcional)**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

## ▶️ Executando o App

```bash
streamlit run Home.py
```

---

## 📦 Requisitos

- Python 3.8+
- Pacotes: streamlit, pandas, plotly, openpyxl (para Excel)

---

## 🧠 Exemplo de Uso
1. Acesse a aba Visualizar Dados e carregue seu .csv ou .xlsx
2. Vá para Limpeza de Dados para tratar valores nulos e colunas
3. Visualize os dados com gráficos na aba Dashboard Analítico
4. Exporte o resultado final em Exportar Resultado

--- 

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo de licença para mais detalhes.  
[Leia a Licença MIT](./LICENSE)

---

## 🤝 Contribuições
Pull requests são bem-vindas. Para mudanças importantes, abra uma issue para discutir o que você gostaria de modificar.