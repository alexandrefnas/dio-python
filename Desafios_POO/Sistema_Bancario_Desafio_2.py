import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# >> Classes <<
# > Classe Cliente
class Cliente:
    def __init__(self, enderco):
        self._endereco = enderco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco
    
   
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) # Recebe conta e trasação

    def adicionar_conta(self, conta):
        self._contas.append(conta) # Adiciona conta no array de conta
# <

# > Classe Pessoa Física filha da classe Cliente
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._contas = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def contas(self):
        return self._contas
# <

# > Classe Transação
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass
# <

# > Classe Saque filha da classe Transação
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
# <

# > Classe Deposito filha da classe Transação
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        self.transacao = "Deposito"

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
# <

# > Classe Historico
class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                # "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
# <

# > Classe Conta
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False    
# <

# >> Classe Conta corrente filha da Classe Conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.
                __name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(f"\n@@@ Operação cancelada!\n O Limite de sáque é de R$ {self._limite_saques:.2f} @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)    
        
        return False
    
    def __str__(self):
        return  f"""\
                    Agência:\t{self.agencia}
                    C/C:\t\t{self.numero}
                    Titular:\t{self.cliente.nome}\
        """        
# <
# <<
    
retorno = "\n Tecle ENTER para voltar ao Menu Principal!"
valor_invalido = "\n O valor informado é invalido!\n O valor aceito é numérico e com as duas casas\n decimais do lado direito do ponto. Ex: 1100.00\n Tente novamente!\n"   

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

def buscar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    print(f"Cliente: {cliente.nome}\n")
    entrada = input(" Informe o valor do depósito: ")
    if not verificar_float(entrada):
        print(valor_invalido)
        # input(retorno)
    else:
        valor = float(entrada)
        transacao = Deposito(valor)
        conta = buscar_conta_cliente(cliente)

        if not conta:
            return

        cliente.realizar_transacao(conta, transacao)
        # input(retorno)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = buscar_conta_cliente(cliente)
    if not conta:
        return
    
    print(f"Cliente: {cliente.nome}\n")
    entrada = input(" Informe o valor do saque: ")
    if not verificar_float(entrada):
        print(valor_invalido)
        input(retorno)
    else:
        valor = float(entrada)
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)
        
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = buscar_conta_cliente(cliente)
    if not conta:
        return

    transacoes = conta.historico.transacoes
    extrato = ""

    if not transacoes:
        extrato = " Não encontramos nenhuma operação no período!"
    else:
        print(f"Cliente: {cliente.nome}\n")
        for trasacao in transacoes:
            extrato += f"{trasacao['tipo']}\t\tR$ {trasacao['valor']:.2f}\n"

    print(extrato)  
    print("─" * 49)
    print(f" Saldo atual:\t\tR$ {conta.saldo:.2f}")
    print("═" * 49)

def criar_cliente(clientes):
   
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("=== Cliente criado com sucesso! ===")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(numero_conta, clientes, contas):
   
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
        
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):    
    for conta in contas:                
        print(textwrap.dedent(str(conta)))
        print("═" * 49)

def main():
    
    clientes = []
    contas = []
    

    while True:
        print("\033c", end="")
        opcao = menu()

        if opcao == "d":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                    Depósito                   ║")
            print("╚═══════════════════════════════════════════════╝")
            print()
            depositar(clientes)
            input(retorno)

        elif opcao == "s":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                     Saque                     ║")
            print("╚═══════════════════════════════════════════════╝")
            # LIMITE_SAQUES = ContaCorrente.limite_saques
            # limite = ContaCorrente.limite
            # numero_saques = 0
            # print(f" Operações diária disponível: {LIMITE_SAQUES - numero_saques }/{LIMITE_SAQUES}.")
            # print(f" Limite de saque por operação: R$ {limite:.2f}\n")
            sacar(clientes)
            input(retorno)

        elif opcao == "e":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                    Extrato                    ║")
            print("╚═══════════════════════════════════════════════╝")   
            print()
            exibir_extrato(clientes)
            input(retorno)

        elif opcao == "nu":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║              Cadastro de Clientes             ║")
            print("╚═══════════════════════════════════════════════╝")
            print()
            criar_cliente(clientes)
            input(retorno)

        elif opcao == "nc":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║               Cadastro de Contas              ║")
            print("╚═══════════════════════════════════════════════╝")
            print()
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            input(retorno)

        elif opcao == "lc":
            print("\033c", end="")
            print("╔═══════════════════════════════════════════════╗")
            print("║                Tabela de Contas               ║")
            print("╚═══════════════════════════════════════════════╝")    
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