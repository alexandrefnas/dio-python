from datetime import date,datetime

data = date(2023, 7, 10)
print(data)

print(data.today())

data_hora = datetime.now() #(2023, 7, 10, 10, 30, 20)
print(data_hora)
print(data_hora.date()) #.today())
print(data_hora.time())
print(data_hora.hour)