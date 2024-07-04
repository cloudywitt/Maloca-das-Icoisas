import os

remedios = []


class EmptyNameError(ValueError):
    pass


class InvalidPriceError(ValueError):
    pass


def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")


def print_menu():
    print("""
███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░██╗░░░░░░█████╗░░█████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗
█████╗░░███████║██████╔╝██╔████╔██║███████║██║░░░░░██║░░██║██║░░╚═╝███████║
██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░░░░██║░░██║██║░░██╗██╔══██║
██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝""")
    print("1. Cadastrar remédio")
    print("2. Listar remédios")
    print("3. Alterar estado do remédio")
    print("4. Sair")


def pegar_opcao():
    try:
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                cadastrar_remedio()
            case 2:
                listar_remedios()
            case 3:
                alterar_estado_remedio()
            case 4:
                sair_do_programa()
            case _:
                limpar_tela()

                print("Escolha uma das opções")
    except ValueError:
        limpar_tela()

        print("Opção inválida: tente outra")

    except KeyboardInterrupt:
        sair_do_programa()

    input("\nDigite uma tecla para voltar ao menu ")


def cadastrar_remedio():
    limpar_tela()

    print("-- Cadastrar remédio --")

    try:
        remedio_nome = input("Nome: ")

        if not remedio_nome:
            raise EmptyNameError

        preco_remedio = float(input("Preço: "))

        if preco_remedio < 0:
            raise InvalidPriceError

        remedio = {
            "nome": remedio_nome,
            "preco": preco_remedio,
            "ativo": False
        }

        remedios.append(remedio)

        limpar_tela()

        print(f"{remedio_nome} foi adicionado com sucesso!")
    except EmptyNameError:
        limpar_tela()

        print("ERRO: o remédio precisa de nome.")
    except InvalidPriceError:
        limpar_tela()

        print("ERRO: preço inválido de remédio.")


def listar_remedios():
    limpar_tela()

    print("-- Remédios --")

    for idx, remedio in enumerate(remedios):
        print(
            f" {idx + 1}. Nome: {remedio['nome']}" +
            f" - Preço: {remedio['preco']:.2f}" +
            f" - Status: {remedio['ativo']}"
        )


def alterar_estado_remedio():
    limpar_tela()

    try:
        remedio_id = int(input("Número do remédio a ser alterado: "))

        if remedio_id < 1:
            raise IndexError

        remedio_id -= 1

        remedio_status = remedios[remedio_id]["ativo"]
        remedios[remedio_id]["ativo"] = not remedio_status

        limpar_tela()

        print(f"Estado de {remedios[remedio_id]['nome']} alterado.")
    except ValueError:
        limpar_tela()

        print("ERRO: Digite um número.")
    except IndexError:
        limpar_tela()

        print("ERRO: remédio não encontrado.")


def sair_do_programa():
    print("\nObrigado pela preferência!")

    exit(0)


def main():
    limpar_tela()
    print_menu()
    pegar_opcao()


if __name__ == '__main__':
    while True:
        main()
