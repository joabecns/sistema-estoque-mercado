import estoque
from time import sleep

def main(dados_estoque: dict):
    while True:
        print("\n" + "=" * 40)
        print("SUPERMERCADO DO SEU ZÉ".center(40))
        print(f"{'\033[1;36m'}MENU DO ADMINISTRADOR{'\033[m'}".center(49))
        print("=" * 40)
        print("[1] Ver estoque completo")
        print("[2] Adicionar / atualizar produto")
        print("[3] Remover produto")
        print("[0] Sair")
        print("=" * 40)

        try:
            opcao = int(input("Insira o número da opção desejada: "))
        except ValueError:
            print(f"{'\033[1;31m'}Erro: Digite apenas números, não letras.{'\033[m'}")
            print()
            continue

        if opcao == 1:
            estoque.mostrar_estoque(dados_estoque)
            input(f'Aperte {'\033[1m'}ENTER{'\033[m'} para voltar ao MENU...')
            print()

        elif opcao == 2:
            estoque.adicionar_item(dados_estoque)

        elif opcao == 3:
            estoque.remover_item(dados_estoque)
 
        elif opcao == 0:
            print("Saindo do painel admim...") 
            sleep(1.5)
            print(f"{'\033[1m'}Até mais!{'\033[m'}")
            break
        else:
            print("Opção inválida. Tente novamente!")


dados_estoque = estoque.carregar_estoque()
main(dados_estoque)
