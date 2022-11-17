import playsound
from forex_python.converter import CurrencyRates
import time 

kur = CurrencyRates()

ilk=kur.get_rate('USD','TRY')
print(ilk)

while True:
    son=kur.get_rate('USD','TRY')
    print(son)
    if son>ilk:
        print(son)
        playsound('alarm.waw')
        
        ilk=son
    time.sleep(2)