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