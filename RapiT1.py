#Aleatorio RapiT1.py

import random
	
print ("Hello Navigators")
from datetime import datetime

fecha_actual = datetime.now()
print("Fecha actual:", fecha_actual)

import random

numeros_aleatorios = [random.randint(1, 50) for _ in range(6)]

print("Seis números aleatorios:", numeros_aleatorios)


while True:
     numeros_aleatorios = [random.randint(1, 50)  for _ in range(6)] # Genera 6 números aleatorios entre 1 y 50
     
     print("Seis Números aleatorios:", numeros_aleatorios)
     input("Presiona Enter para continur")
     
#import random

# l.Let's generate 6 values between 0 and 50. Store valued on a list.random

#my_list = []

#for _ in range (6):
  #rand_num = random.randint(1, 50)
  #my_list.append(rand_num)

