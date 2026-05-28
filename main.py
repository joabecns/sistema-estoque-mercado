import estoque
from time import sleep

def main(dados_estoque: dict):
    print("=" * 40)
    print("SUPERMERCADO DO SEU ZÉ".center(35))
    print("=" * 40)
    print()

    while True:
        print("=" * 40)
        print("MENU DO ADMINISTRADOR".center(35))
        print("=" * 40)
        print("[1] Ver estoque completo")
        print("[2] Adicionar / atualizar produto")
        print("[3] Remover produto")
        print("[0] Sair")
        print()

        try:
            opcao = int(input("Insira o número da opção desejada: "))
        except ValueError:
            print("Digite um número, não letras")
            print()
            continue

        if opcao == 1:
            estoque.mostrar_estoque(dados_estoque)

        elif opcao == 2:
            estoque.adicionar_item(dados_estoque)

        elif opcao == 3:
            estoque.remover_item(dados_estoque)
 
        elif opcao == 0:
            print("Saindo do painel admim...") 
            sleep(1.5)
            break
        else:
            print("Opção inválida.")


dados_estoque = estoque.carregar_estoque()
main(dados_estoque)
