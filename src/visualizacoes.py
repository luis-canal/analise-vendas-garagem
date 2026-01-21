import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


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

def grafico_metodo_venda(df, frame):
    vendas = df["forma_pagamento"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    vendas.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Distribuição por Método de Venda")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

def grafico_tempo_estoque(df, frame):
    df["data_entrada"] = pd.to_datetime(df["data_entrada"])
    df["data_venda"] = pd.to_datetime(df["data_venda"])
    df["tempo_estoque"] = (df["data_venda"] - df["data_entrada"]).dt.days

    media = df.groupby("modelo")["tempo_estoque"].mean()

    fig, ax = plt.subplots(figsize=(6, 4))
    media.plot(kind="bar", ax=ax)

    ax.set_title("Tempo Médio de Estoque por Modelo")
    ax.set_ylabel("Dias")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

def grafico_troca(df, frame):
    troca = df["troca"].value_counts()

    fig, ax = plt.subplots(figsize=(5, 4))
    troca.plot(kind="bar", ax=ax)

    ax.set_title("Vendas com Troca vs Sem Troca")
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