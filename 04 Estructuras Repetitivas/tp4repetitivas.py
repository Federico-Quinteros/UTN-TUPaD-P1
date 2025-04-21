import math, random

# Actividad 1

for i in range (101):
    print(i)


# Actividad 2

numero = int(input("Ingrese un número: "))
digitos = 0
while numero != 0:
    numero = math.trunc(numero / 10)
    digitos += 1

print(f"El número contiene {digitos} digitos!")

# Actividad 3

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
suma = 0

for i in range (numero1+1,numero2):
    suma += i

print (f"La suma de los números comprendidos entre los números ingresados es igual a {suma}")

# Actividad 4

numero = int(input("Ingrese un número entero que desee sumar (0 para terminar): "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número que desee sumar (0 para terminar): "))

print (f"La suma de los números ingresados es igual a {suma}")

# Actividad 5  

numeroRandom = random.randint(0,9)
numero = int(input("Ingrese un número entre 0 y 9 para adivinar el número aleatorio: "))
intentos = 1

while numeroRandom != numero:
    intentos += 1
    numero = int(input("Ingrese un número entre 0 y 9 para adivinar el número aleatorio: "))

print(f"Usted adivino el número aleatorio en {intentos} intentos!")

# Actividad 6

for i in range (101,-1,-1):
    if i % 2 == 0:
        print(i)

# Actividad 7

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero):
    suma += i

print (f"La suma de los números comprendidos entre 0 y {numero} es igual a {suma}")

# Actividad 8

positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range (10):
    numero = int(input("Ingrese un número entero: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    elif numero % 2 != 0:  
        impares += 1

print("De los números ingresados")
print(F"{pares} números son pares")
print(F"{impares} números son impares")
print(F"{positivos} números son positivos")
print(F"{negativos} números son negativos")

# Actividad 9

suma = 0 
cantidad = 0
for i in range (10):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
    cantidad += 1

print(f"La media de los valosres ingresados es igual a",(suma/cantidad))

# Actividad 10

numero = int(input("Ingrese un número: "))
inverso = 0
digito = 0

while numero != 0:
    digito = numero % 10
    numero = math.trunc(numero/10)
    inverso = inverso * 10 + digito

print(f"El número ingresado es {numero}")
print(f"El número ingresado invertido es {inverso}")
