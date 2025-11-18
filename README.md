# Radio Favorites Parser — Automação de Organização de Rádios

Este projeto automatiza a extração e organização de rádios brasileiras a partir do arquivo **HTML exportado dos favoritos do navegador** (Chrome/Brave).  
O script lê todas as entradas `<A>` do arquivo, interpreta nome da rádio, cidade, UF e link, e gera uma **planilha completamente estruturada** em poucos segundos.

Ideal para quem monitora rádios, faz catalogação ou precisa organizar grandes conjuntos de links rapidamente.

---

## Funcionalidades

- Leitura automática do arquivo HTML de favoritos do navegador.
- Extração confiável dos dados:
  - Nome da rádio  
  - Cidade  
  - UF  
  - Link  
- Regex robusta para tratar formatos do tipo:  
  **"Rádio X - Cidade / UF - Brasil | Radios.com.br"**
- Geração de arquivo Excel estruturado (`.xlsx`).
- Coluna *Status* deixada em branco para preenchimento posterior.
- Não precisa editar o HTML manualmente.

---

## Estrutura de Saída (Excel)

O arquivo gerado contém as colunas:

| UF | Cidade | Rádio (com frequência) | Link | Status |
|----|--------|-------------------------|------|--------|

Você pode abrir o Excel, clicar no quadradinho do canto superior esquerdo e aplicar uma formatação de tabela rapidamente.

---

## Como funciona internamente

O script utiliza:

- **BeautifulSoup** → parsing do HTML  
- **Regex (re)** → extração estruturada dos campos  
- **Pandas** → criação da tabela final  
- **openpyxl** → exportação para Excel  

A expressão regular usada para capturar os dados é:

```python
r"^(.*?)\s*-\s*(.*?)\s*/\s*([A-Z]{2})"
