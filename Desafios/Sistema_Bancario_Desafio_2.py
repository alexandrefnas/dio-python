import textwrap

def verificar_float(val):
    try:
        numero = float(val)
        return "{:.2f}".format(numero) == val
    except ValueError:
        return False
    
def menu():
    menu = """\n
    ╔═══════════════════════════════════════════════╗
    ║                 MENU BANCÁRIO                 ║
    ╠═══════════════════════════════════════════════╣
    ║  [d ]  Depositar                              ║
    ║  [s ]  Sacar                                  ║
    ║  [e ]  Extrato                                ║
    ║  [nc]  Nova conta                             ║
    ║  [lc]  Listar contas                          ║
    ║  [nu]  Novo usuário                           ║
    ║  [q ]  Sair                                   ║
    ╚═══════════════════════════════════════════════╝
     Digite umas das opções entre [ ] acima
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f" Depósito:\t\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print(f"\n@@@ Operação cancelada!\n O Limite de sáque é de R$ {limite:.2f} @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f" Saque:\t\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        # print(numero_saques)
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\033c", end="")
    print("╔═══════════════════════════════════════════════╗")
    print("║                    Extrato                    ║")
    print("╚═══════════════════════════════════════════════╝")   
    print(" Não foi encontrado nenhuma operação no período!" if not extrato else extrato)
    print("─" * 49)
    print(f" Saldo atual:\t\tR$ {saldo:.2f}")
    print("═" * 49)

def criar_usuario(usuarios):
    print("\033c", end="")
    print("╔═══════════════════════════════════════════════╗")
    print("║              Cadastro de Usuários             ║")
    print("╚═══════════════════════════════════════════════╝")
    print()
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    print("\033c", end="")
    print("╔═══════════════════════════════════════════════╗")
    print("║               Cadastro de Contas              ║")
    print("╚═══════════════════════════════════════════════╝")
    print()
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    print("\033c", end="")
    print("╔═══════════════════════════════════════════════╗")
    print("║                Tabela de Contas               ║")
    print("╚═══════════════════════════════════════════════╝")    
    for conta in contas:        
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}\
        """        
        print(textwrap.dedent(linha))
        print("═" * 49)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    retorno = "\n Tecle ENTER para voltar ao Menu Principal!"
    valor_invalido = "\n O valor informado é invalido!\n O valor aceito é numérico e com as duas casas\n decimais do lado direito do ponto. Ex: 1100.00\n Tente novamente!\n"

    while True:
        print("\033c", end="")
        opcao = menu()

        if opcao == "d":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                    Depósito                   ║")
            print("╚═══════════════════════════════════════════════╝")
            print()
            entrada = input(" Informe o valor do depósito: ")
            if not verificar_float(entrada):
                print(valor_invalido)
                input(retorno)
            else:
                valor = float(entrada)
                saldo, extrato = depositar(saldo, valor, extrato)
                input(retorno)

        elif opcao == "s":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                     Saque                     ║")
            print("╚═══════════════════════════════════════════════╝")
            print(f" Operações diária disponível: {LIMITE_SAQUES - numero_saques }/{LIMITE_SAQUES}.")
            print(f" Limite de saque por operação: R$ {limite:.2f}\n")

            entrada = input(" Informe o valor do saque: ")
            if not verificar_float(entrada):
                print(valor_invalido)
                # input(retorno)
            else:
                valor = float(entrada)

                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            input(retorno)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            input(retorno)

        elif opcao == "nu":
            criar_usuario(usuarios)
            input(retorno)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

            input(retorno)

        elif opcao == "lc":
            listar_contas(contas)
            input(retorno)

        elif opcao == "q":
            print("\n Obrigado por usar os nossos servíços!")
            input()
            print("\033c", end="")
            break

        else:
            print("\n Operação inválida, por favor, selecionar novamente a operação desejada.")
            input(retorno)

main()