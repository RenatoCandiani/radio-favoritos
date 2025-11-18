from bs4 import BeautifulSoup
import pandas as pd
import re

def extrair_dados_texto(texto):
    padrao = r"^(.*?)\s*-\s*(.*?)\s*/\s*([A-Z]{2})"
    m = re.search(padrao, texto)

    if not m:
        return None, None, None
    
    radio = m.group(1).strip()
    cidade = m.group(2).strip()
    uf = m.group(3).strip()
    return radio, cidade, uf


def processar_favoritos_html(arquivo_html, saida_excel="radios_organizadas.xlsx"):
    with open(arquivo_html, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    registros = []

    for a in soup.find_all("a"):
        texto = a.get_text(strip=True)
        url = a.get("href")

        parsed = extrair_dados_texto(texto)

        if parsed == (None, None, None):
            continue

        radio, cidade, uf = parsed

        registros.append({
            "UF": uf,
            "Cidade": cidade,
            "Rádio (com frequência)": radio,
            "Link": url,
            "Status": ""
        })

    df = pd.DataFrame(registros, columns=[
        "UF", "Cidade", "Rádio (com frequência)", "Link", "Status"
    ])

    df.to_excel(saida_excel, index=False)
    print(f"Arquivo gerado: {saida_excel}")


if __name__ == "__main__":
    processar_favoritos_html("favoritos.html")