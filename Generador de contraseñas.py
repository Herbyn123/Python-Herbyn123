import random

print("Soy un programa que genera contraseñas") # Saludo normal 

name = input(print("Escribe tu nombre:"))

password1  = int(input(print("Introduce la longitud de la contraseña:")))

password2 = "";

generador = "qwertyuiopasdfghjklzxcvbnm123456789ASDFGHJK"

for i in range(password1):
    password2+=random.choice(generador)

print(name + password2)