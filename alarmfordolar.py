

import playsound #library to sound the alarm 
from forex_python.converter import CurrencyRates #The library that allows us to get the current rate 
import time #To slow down the while loop 

rate = CurrencyRates() # describing 

first=rate.get_rate('USD','TRY') # Get current rate
print(first)



while True:

    last=rate.get_rate('USD','TRY')
    print(last)

    if last>first:
        print(last)
        playsound('alarm.waw')
        first=last

    time.sleep(2)
