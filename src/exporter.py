import base64
from io import BytesIO

def get_download_link(df):
    output = BytesIO()
    df.to_excel(output, index=False, engine="openpyxl")
    output.seek(0)
    b64 = base64.b64encode(output.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="dados_limpos.xlsx">📥 Baixar arquivo Excel</a>'
    return href
