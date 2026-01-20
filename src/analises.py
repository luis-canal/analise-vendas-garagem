import pandas as pd


def carregar_dados(caminho_arquivo):
    """Carrega o dataset de vendas"""
    return pd.read_csv(caminho_arquivo)


def mostrar_metricas_gerais(df):
    total_vendas = len(df)
    faturamento_total = df["preco"].sum()
    ticket_medio = df["preco"].mean()

    print("MÉTRICAS GERAIS")
    print("----------------")
    print(f"Total de vendas: {total_vendas}")
    print(f"Faturamento total: R$ {faturamento_total:,.2f}")
    print(f"Ticket médio: R$ {ticket_medio:,.2f}")


def vendas_por_modelo(df):
    print("\nVENDAS POR MODELO")
    print("-----------------")
    print(df["modelo"].value_counts())


def vendas_por_pagamento(df):
    print("\nVENDAS POR FORMA DE PAGAMENTO")
    print("----------------------------")
    print(df["forma_pagamento"].value_counts())


def vendas_por_cidade(df):
    print("\nVENDAS POR CIDADE")
    print("----------------")
    print(df["cidade"].value_counts())