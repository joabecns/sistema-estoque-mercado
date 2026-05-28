import json
import os
from time import sleep

arquivo = "estoque.json"

estoque_padrao = {
    "arroz":{"preco": 25.9, "quantidade": 50},
    "feijão":{"preco": 8.5, "quantidade": 80},
    "leite integral":{"preco": 5.2, "quantidade": 120},
    "óleo de soja":{"preco": 7.8, "quantidade": 60},
    "açúcar":{"preco": 4.9, "quantidade": 100},
    "macarrão":{"preco": 3.5, "quantidade": 75},
    "café": {"preco": 14.9, "quantidade": 40},
    "farinha":{"preco": 4.2, "quantidade": 87},
    "sabão em pó":{"preco": 11.5, "quantidade": 35},
    "chocolate": {"preco": 5.0, "quantidade": 30}
}

def mostrar_estoque(estoque_padrao: dict):
    print("=" * 50)
    print(f"{'PRODUTO':<20} | {'PREÇO':<12} | {'QUANTIDADE':<10}")
    print("=" * 50)

    for produto, dados in sorted(estoque_padrao.items()):
        print(f"{produto:<20} | R${dados['preco']:<10} | {dados['quantidade']:<10}")

    print("=" * 50)

def salvar_estoque(estoque_padrao: dict):
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque_padrao, arquivo, indent=4, ensure_ascii=False)

def carregar_estoque():
    if not os.path.exists("estoque.json"):
        salvar_estoque(estoque_padrao)
        return estoque_padrao

    with open("estoque.json", "r", encoding="utf-8") as arquivo:
        estoque = json.load(arquivo)
        return estoque

def adicionar_item(estoque: dict):
    print()
    print("--- ADICIONAR / ATUALIZAR PRODUTO ---")
    print()
    mostrar_estoque(estoque)

    nome = input("Nome do produto: ").strip().lower()
            
    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            if preco <= 0:
                print('Valor inváido! Insira novamente')
            else:
                break
        except ValueError:
            print("Preço inválido.")
            return
        
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade <= 0:
                print('Valor inváido! Insira novamente')
            else:
                break
        except ValueError:
            print("Quantidade inválida.")
            return

    if nome in estoque:
        status = 'ATUALIZADO'
    else:
        status = 'ADICIONADO'
    estoque[nome] = {"preco": preco, "quantidade": quantidade}
    salvar_estoque(estoque)
    sleep(1.5)
    print(f"O produto '{nome}' foi {'\033[32m'}{status}{'\033[m'} com sucesso!")
    input('Aperte ENTER para voltar ao MENU...')

def remover_item(estoque: dict):
    print()
    print("--- REMOVER PRODUTO ---")
    mostrar_estoque(estoque)
    print()
    nome = input("Nome do produto a remover: ").strip().lower()

    if nome in estoque:
        confirma = input(f"Confirma remoção de '{nome}'? (s/n): ").strip().lower()[0]
        if confirma == "s":
            del estoque[nome]
            salvar_estoque(estoque)
            sleep(1.5)
            print(f"O produto '{nome}' foi {'\033[31m'}REMOVIDO{'\033[m'} com sucesso!")
            input('Aperte ENTER para voltar ao MENU...')
        else:
            print("Operação cancelada.")
    else:
        print("Produto não encontrado no estoque")

