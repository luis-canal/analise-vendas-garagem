import tkinter as tk
import pandas as pd
from visualizacoes import grafico_vendas_por_modelo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard - Análise de Vendas da Garagem")
        self.geometry("1000x600")
        self.configure(bg="#f0f0f0")

        self.criar_layout()
    
    def carregar_dados(self):
        return pd.read_csv("data/vendas.csv")

    def criar_layout(self):
        # Menu lateral
        self.menu = tk.Frame(self, bg="#2c3e50", width=220)
        self.menu.pack(side="left", fill="y")

        # Área principal
        self.conteudo = tk.Frame(self, bg="white")
        self.conteudo.pack(side="right", expand=True, fill="both")

        # Título do menu
        titulo_menu = tk.Label(
            self.menu,
            text="MENU",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 14, "bold")
        )
        titulo_menu.pack(pady=20)

        # Botões do menu
        botoes = [
            ("Visão Geral", self.visao_geral),
            ("Métodos de Venda", self.metodos_venda),
            ("Tempo de Estoque", self.tempo_estoque),
            ("Troca", self.troca),
        ]

        for texto, comando in botoes:
            btn = tk.Button(
                self.menu,
                text=texto,
                command=comando,
                bg="#34495e",
                fg="white",
                font=("Arial", 11),
                relief="flat",
                padx=10,
                pady=10
            )
            btn.pack(fill="x", padx=10, pady=5)

    def limpar_conteudo(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    def visao_geral(self):
        self.limpar_conteudo()

        df = self.carregar_dados()

        titulo = tk.Label(
            self.conteudo,
            text="Visão Geral das Vendas",
            font=("Arial", 18),
            bg="white"
        )
        titulo.pack(pady=10)

        grafico_vendas_por_modelo(df, self.conteudo)

    def metodos_venda(self):
        self.limpar_conteudo()
        label = tk.Label(
            self.conteudo,
            text="Análise dos Métodos de Venda",
            font=("Arial", 18),
            bg="white"
        )
        label.pack(pady=20)

    def tempo_estoque(self):
        self.limpar_conteudo()
        label = tk.Label(
            self.conteudo,
            text="Tempo de Estoque dos Veículos",
            font=("Arial", 18),
            bg="white"
        )
        label.pack(pady=20)

    def troca(self):
        self.limpar_conteudo()
        label = tk.Label(
            self.conteudo,
            text="Vendas com Troca vs Sem Troca",
            font=("Arial", 18),
            bg="white"
        )
        label.pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
