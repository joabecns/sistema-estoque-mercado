import json

arquivo = "estoque.json"

estoque_padrao = {
    "arroz 5kg": {"preco": 25.9, "quantidade": 50},
    "feijão 1kg": {"preco": 8.5, "quantidade": 80},
    "leite integral": {"preco": 5.2, "quantidade": 120},
    "óleo de soja": {"preco": 7.8, "quantidade": 60},
    "açúcar 1kg": {"preco": 4.9, "quantidade": 100},
    "macarrão 500g": {"preco": 3.5, "quantidade": 75},
    "café 500g": {"preco": 14.9, "quantidade": 40},
    "farinha de trigo": {"preco": 4.2, "quantidade": 87},
    "sabão em pó": {"preco": 11.5, "quantidade": 35},
    "barra de chocolate": {"preco": 5.0, "quantidade": 30}
}


def mostrar_estoque(estoque_padrao: dict):

    print("=" * 50)
    print(f"{'PRODUTO':<20}{'PREÇO':<10}{'QUANTIDADE':<10}")
    print("=" * 50)

    for produto, dados in sorted(estoque_padrao.items()):

        print(f"{produto:<20}{dados['preco']:<10}{dados['quantidade']:<10}")

    print("=" * 50)


def salvar_estoque(estoque_padrao: dict):

    with open(arquivo, "w", encoding="utf-8") as arq:

        json.dump(estoque_padrao, arq, indent=4, ensure_ascii=False)


def carregar_estoque():

    with open(arquivo, "r", encoding="utf-8") as arq:

        estoque = json.load(arq)

    return estoque

salvar_estoque(estoque_padrao)
estoque = carregar_estoque()
mostrar_estoque(estoque)