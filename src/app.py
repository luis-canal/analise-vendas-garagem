import tkinter as tk


def main():
    janela = tk.Tk()
    janela.title("Análise de Vendas - Garagem")
    janela.geometry("800x500")

    label = tk.Label(
        janela,
        text="Dashboard de Análise de Vendas",
        font=("Arial", 16)
    )
    label.pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    main()