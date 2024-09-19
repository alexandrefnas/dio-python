def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome ="Anônimo"):
    print(f"Seja bem vindo {nome}!")


nome = "Alexandre"
exibir_mensagem()
exibir_mensagem_2(nome)
exibir_mensagem_3()


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

marca = "Fiat"
modelo = "Pálio"
ano = 1999
placa = "ABC-1234"

print(salvar_carro(marca, modelo, ano, placa))

