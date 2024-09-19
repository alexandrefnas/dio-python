menu = """
╔═════════════════════════════════╗
║          MENU Bancário          ║
╚═════════════════════════════════╝
  [d] Depositar  
  [s] Sacar      
  [e] Extrato       
  [q] Sair       

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\033c", end="")
    opcao = input(menu)

    if opcao == "d":
        print("\033c", end="")
        print("╔═════════════════════════════════╗")
        print("║             Depósito            ║")
        print("╚═════════════════════════════════╝")
        print()
        valor = (input("Digite o valor: "))
        
        if float(valor) > 0:
            saldo += valor
            extrato += f" Deposito:        +R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
            input()

        else:
            print(" Operação cancelada!\n Valor invalido!")
            input()
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("\033c", end="")
            print("╔═════════════════════════════════╗")
            print("║              Saque              ║")
            print("╚═════════════════════════════════╝")
            print()
            valor = float(input("Digite o valor: "))
            if valor > limite:
                print(" Operação cancelada!\n O Limite de sáque é de R$ 500,00")
                input()
            elif valor > saldo:
                print("Saldo insuficiente para saque!")
                input()

            elif valor > 0:
                saldo -= valor
                numero_saques += 1
                extrato += f" Saque:           -R$ {valor:.2f}\n"
                print("Saque realizado com sucesso!")
                input()
            else:
                print(" Operação cancelada!\n Valor invalido!")
                input()

        else:
            print("Excedeu o limíte de sáque diário!")
            input()
    elif opcao == "e":
        print("\033c", end="")
        print("╔═════════════════════════════════╗")
        print("║             Extrato             ║")
        print("╚═════════════════════════════════╝")
        print("Não foi encontrado nenhuma\noperação no período!" if not extrato else extrato)
        print("──────────────────────────────────")
        print(f" Saldo atual:    R$ {saldo:.2f}")
        print("══════════════════════════════════")
        input()

    elif opcao == "q":
        print("Obrigado por usar os nossos servíços!")
        input()
        break

    else:
        print("Operação inválida, por favor, selecionar novamente a operação desejada.")
        input()