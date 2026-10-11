Lê o ficheiro original (pd.read_excel).

Limpa as repetições (drop_duplicates) e formata os textos e espaços vazios (str.strip(), fillna).

Guarda automaticamente num novo ficheiro limpo (to_excel).

E, para o utilizar no dia a dia com um ficheiro diferente, basta alterar o nome entre as aspas na linha de execução:

Python
resultado = limpar_excel_real("o_teu_novo_ficheiro.xlsx")
