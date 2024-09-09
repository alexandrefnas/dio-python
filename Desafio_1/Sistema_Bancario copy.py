def verificar_float(val):
    try:
        numero = float(val)
        return "{:.2f}".format(numero) == val
    except ValueError:
        return False

menu = """
╔═════════════════════════════════════════╗
║              MENU Bancário              ║
╚═════════════════════════════════════════╝
  [d] Depositar  
  [s] Sacar      
  [e] Extrato       
  [q] Sair       

  Digite umas das opções entre [ ] acima
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
retorno = "\n Tecle ENTER para voltar ao Menu Principal!"
valor_invalido = "\n O valor informado é invalido!\n O valor aceito é numérico e com as duas casas\n decimais do lado direito do ponto. Ex: 1100.00\n Tente novamente!\n"

while True:
    print("\033c", end="")
    opcao = input(menu)
    if opcao == "d":
        print("\033c", end="")
        print("╔═════════════════════════════════════════╗")
        print("║                 Depósito                ║")
        print("╚═════════════════════════════════════════╝")
        print()
        entrada = input("Digite o valor: ")
        if not verificar_float(entrada):
            print(valor_invalido)
            input(retorno)
        else:
            valor = float(entrada)
            if valor > 0:
                saldo += valor
                extrato += f" Deposito:        +R$ {valor:.2f}\n"
                print("\n Depósito realizado com sucesso!")
                input(retorno)
            else:
                print("\n Operação cancelada!\n Valor invalido!!")
                input(retorno)

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("\033c", end="")
            print("╔═════════════════════════════════════════╗")
            print("║                  Saque                  ║")
            print("╚═════════════════════════════════════════╝")
            print(f" Operações diária disponível: {3 - numero_saques }/{LIMITE_SAQUES}.")
            print(f" Limite de saque por operação: R$ {limite:.2f}\n")
            entrada = input(" Digite o valor: ")
            if not verificar_float(entrada):
                print(valor_invalido)
                input(retorno)
            else:
                valor = float(entrada)
                if valor > limite:
                    print(f"\n Operação cancelada!\n O Limite de sáque é de R$ {limite:.2f}")
                    input(retorno)
                elif valor > saldo:
                    print("\n Saldo insuficiente para saque!")
                    input(retorno)
                elif valor > 0:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f" Saque:           -R$ {valor:.2f}\n"
                    print("\n Saque realizado com sucesso!")
                    input(retorno)
                else:
                    print("\n Operação cancelada!\n Valor invalido!")
                    input(retorno)

        else:
            print("\n Excedeu o limíte de sáque diário!")
            input(retorno)

    elif opcao == "e":
        print("\033c", end="")
        print("╔═════════════════════════════════╗")
        print("║             Extrato             ║")
        print("╚═════════════════════════════════╝")
        print("Não foi encontrado nenhuma\noperação no período!" if not extrato else extrato)
        print("──────────────────────────────────")
        print(f" Saldo atual:    R$ {saldo:.2f}")
        print("══════════════════════════════════")
        input(retorno)
    elif opcao == "q":
        print("\n Obrigado por usar os nossos servíços!")
        input()
        print("\033c", end="")
        break
    else:
        print("\n Operação inválida, por favor, selecionar novamente a operação desejada.")
        input(retorno)