from analises import (
    carregar_dados,
    mostrar_metricas_gerais,
    vendas_por_cidade,
    vendas_por_modelo,
    vendas_por_pagamento,
)

def main():
    df = carregar_dados("data/vendas.csv")

    mostrar_metricas_gerais(df)
    vendas_por_modelo(df)
    vendas_por_pagamento(df)
    vendas_por_cidade(df)

if __name__ == "__main__":
    main()
