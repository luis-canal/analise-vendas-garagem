import matplotlib.pyplot as plt

def grafico_vendas_por_modelo(df):
    vendas = df["modelo"].value_counts()
    
    plt.figure()
    vendas.plot(kind="bar")
    plt.title("Vendas por Modelo")
    plt.xlabel("Modelo")
    plt.ylabel("Quantidade de Vendas")
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_pagamento(df):
    vendas = df["forma_pagamento"].value_counts()

    plt.figure()
    vendas.plot(kind="bar")
    plt.title("Vendas por Forma de Pagamento")
    plt.xlabel("Forma de Pagamento")
    plt.ylabel("Quantidade de Vendas")
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_cidade(df):
    vendas = df["cidade"].value_counts()

    plt.figure()
    vendas.plot(kind="bar")
    plt.title("Vendas por Cidade")
    plt.xlabel("Cidade")
    plt.ylabel("Quantidade de Vendas")
    plt.tight_layout()
    plt.show()