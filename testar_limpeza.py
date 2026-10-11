import pandas as pd

def limpar_excel_real(caminho_ficheiro, caminho_saida="novos_dados_limpos.xlsx"):
    print(f"A ler o ficheiro real: {caminho_ficheiro}...")
    
    # 1. Lê o seu ficheiro Excel verdadeiro
    df = pd.read_excel(caminho_ficheiro)
    
    print(f"Dimensões originais: {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
    # 2. Remover duplicados com base na coluna 'nome' (mantém o primeiro)
    if 'nome' in df.columns:
        df = df.drop_duplicates(subset=['nome'], keep='first')
    else:
        df = df.drop_duplicates()
        
    # 3. Limpar espaços em branco à volta dos textos
    for coluna in df.select_dtypes(include=["object"]).columns:
        df[coluna] = df[coluna].str.strip()
        
    # 4. Tratar valores em falta (Texto vira "N/D", números viram 0)
    for coluna in df.columns:
        if df[coluna].dtype == "object":
            df[coluna] = df[coluna].fillna("N/D")
        else:
            df[coluna] = df[coluna].fillna(0)
            
    # 5. Guardar o novo ficheiro limpo
    df.to_excel(caminho_saida, index=False)
    print(f"Processo concluído! Ficheiro limpo guardado em: {caminho_saida}")
    
    return df

# --- AQUI É SÓ INDICAR O SEU FICHEIRO REAL ---
resultado = limpar_excel_real("novos_dados.xlsx")

print("\n--- DADOS FINAIS DEPOIS DA LIMPEZA ---")
print(resultado)