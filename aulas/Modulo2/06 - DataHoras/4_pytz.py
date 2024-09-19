# pip install pytz
import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
#mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M:%S"
#mascara_hor = "%H:%M:%S" 
print(data.strftime(mascara_en))
print(data2.strftime(mascara_en))