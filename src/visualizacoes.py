import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def grafico_vendas_por_modelo(df, frame):
    vendas = df["modelo"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    vendas.plot(kind="bar", ax=ax)

    ax.set_title("Vendas por Modelo")
    ax.set_xlabel("Modelo")
    ax.set_ylabel("Quantidade")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)


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