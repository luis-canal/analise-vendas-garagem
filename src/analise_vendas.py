import pandas as pd

df = pd.read_csv("data/vendas.csv")

total_vendas = len(df)
faturamento_total = df["preco"].sum()
ticket_medio = df["preco"].mean()

print("- MÉTRICAS GERAIS -")
print("-------------------")
print(f"Total de vendas: {total_vendas}")
print(f"Faturamento total: {faturamento_total:,.2f}")
print(f"Ticket Médio: {ticket_medio:,.2f}")