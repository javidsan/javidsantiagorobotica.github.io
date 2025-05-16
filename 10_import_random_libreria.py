# import random

# player=input("elije piedra, papel o tijera \n")

# opciones = ["piedra","papel","tijera"]
# juego= random.choice(opciones)
# print(juego)

# if juego == "piedra" and player =="tijera":
#    print("gano la consola")
# elif juego == "papel" and player =="tijera":
#     print("ganaste")
# elif juego == "tijera" and player =="papel":
#    print("gano la consola")
# elif juego == "piedra" and player =="papel":
#    print("ganaste")
# elif juego == "papel" and player =="piedra":
#    print("gano la consola")
# elif juego == "tijera" and player =="piedra":
#    print("ganaste")
# else:
#     print("empate")

# import random
# number = random.randint(1,100)

# while True:
#     adivina=int(input("digita un numero"))
#     if number == adivina:
#         print("has ganado")
#         break
#     elif number < adivina:
#        print("el numero es menor")
       
#     elif number > adivina:
#       print("el numero es mayor")
      

import random

temas=input("digita cualquier cosa")

opciones = ["nvidia","student","titanic","depresion"]
temas= random.choice(opciones)
print(temas)



