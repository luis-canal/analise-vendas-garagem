import pandas as pd

df = pd.read_csv("data/vendas.csv")

total_vendas = len(df)
faturamento_total = df["preco"].sum()
ticket_medio = df["preco"].mean()
vendas_por_modelo = df["modelo"].value_counts()
vendas_pagamento = df["forma_pagamento"].value_counts()

print("- MÉTRICAS GERAIS -")
print("-------------------")
print(f"Total de vendas: {total_vendas}")
print(f"Faturamento total: {faturamento_total:,.2f}")
print(f"Ticket Médio: {ticket_medio:,.2f}")

print("\nVENDAS POR MODELO")
print("-------------------")
print(vendas_por_modelo)

print("\nVENDAS POR FORMA DE PAGAMENTO")
print("-------------------")
print(vendas_pagamento)
