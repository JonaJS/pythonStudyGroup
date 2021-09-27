'''
Entrada y salida de datos.

Como ya vimos en la sesión pasada, la forma en la que nosotros mostramos información por consola es mediante el uso de
la función <print()>. Ahora veremos la función <input()> que nos permitirá pedirle información al usuario para que
podamos trabajar con dicha información.
'''

# Dentro de los paréntesis podemos escribir el mensaje que queramos que aparezca en la consola.
name = input("Enter your name: ")

# Input siempre regresa un objeto del tipo string y podemos comprobarlo consultando el tipo de objeto.
print(type(name))

# Ahora podemos imprimir la variable "name".
print(name)

# Que pasa si queremos imprimir un mensaje junto a nuestra variable? Podemos hacer lo siguiente:
print("Mi nombre es " + name)

'''
input con datos numéricos
'''
# Como dijimos, input regresa un objeto del tipo entero, si queremos ingresar un número, este será de tipo string.
age = input("How old are you? ")
print(type(age))

# Como convertimos este valor a un tipo entero (int)?
# 1.- Cambiando (parsing) el valor de la variable:
age = int(age)
print(type(age))

# 2.- Cambiando directamente el tipo de dato del input:
current_age = int(input("Enter your age: "))
print(type(current_age))

# Podemos imprimir la información completa:
print("Hello, I'm" + " " + str(name) + " and I'm " + str(age) + " years old.")

# Esta forma de imprimir los resultados de alguna operación puede resultar algo díficil, usemos mejor f-strings:
print(f"Hello, I'm {name} and I'm {age} years old.")

# f-strings es una forma mas fácil y natural de imprimir un resultado.


