from datetime import date, datetime, timedelta

tipo_carro = "P" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

#tipo_carro = input("Tipo de carro: ")
if tipo_carro == "P":
    data_estimada = data_atual +timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual +timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

else:
    data_estimada = data_atual +timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days= 1))    
resultado = datetime(2023, 7, 25, 10,19,20) - timedelta(hours=1)
print(resultado.time())

data_hora_str = "2023-10-20 10:20"
data_hora_atual = datetime.now()
data_atual = datetime.now().date()
hora_atual = datetime.now().time()
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"
mascara_hor = "%H:%M:%S" 
print(data_hora_atual.strftime(mascara_ptbr))
print(hora_atual.strftime(mascara_hor))
data_converida = datetime.strptime(data_hora_str, mascara_en)
print(data_converida)
#print(type(data_converida))

