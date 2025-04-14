# Actividad 1
edad = int(input("Ingrese su edad"))
if (edad >= 18):
    print("Es mayor de edad")

#Actividad 2

nota = int(input("Ingrese su nota"))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3

numero = int(input("Ingrese un número par"))
if (numero % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad 4

edad = int(input("Ingrese su edad"))
if (edad > 0 and edad <= 12):
    print("Usted es un niño/a")
elif (edad > 12 and edad <= 17):
    print("Usted es un adolescente")
elif (edad >= 18 and edad <= 30):
    print("Usted es un adulto/a joven")
elif (edad > 30):
    print("Usted es un adulto/a")
else:
    print("Por favor ingrese una edad válida")

#Actividad 5

password = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
if (len(password) >= 8 and len(password) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 

#Actividad 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
if (mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Sesgo positivo o a la derecha")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Sesgo negativo o a la izquierda")
elif (mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios)):
    print("Sin sesgo")
else:
    print("No se cumple ninguna condición")

#Actividad 7

password = input("Por favor ingrese una palabra").lower()
if (password[-1] == "a" or password[-1] == "e" or password[-1] == "i" or password[-1] == "o" or password[-1] == "u"):
    print(f"{password}!")
else:
    print(f"{password}")

#Actividad 8

nombre = input("Por favor ingrese su nombre")
print ("1. Si quiere su nombre en mayúsculas")
print ("2. Si quiere su nombre en minúsculas")
print ("3. Si quiere su nombre con la primera letra mayúscula")
opcion = int(input ("Ingrese la opción deseada"))

if (opcion == 1):
    print(nombre.upper())
elif (opcion == 2):
    print(nombre.lower())
elif (opcion == 3):
    print(nombre.title())
else:
    print("La opción ingresada no es correcta")

#Actividad 9

magnitudTerremoto = float(input("Ingrese la magnitud del terremoto"))
if (magnitudTerremoto < 3):
    print("Muy leve (imperceptible)")
elif (magnitudTerremoto >= 3 and magnitudTerremoto < 4):
    print("Leve (ligeramente perceptible)")
elif (magnitudTerremoto >= 4 and magnitudTerremoto < 5):
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif (magnitudTerremoto >= 5 and magnitudTerremoto < 6):
    print("Fuerte (puede causar daños en estructurasdébiles)")
elif (magnitudTerremoto >= 6 and magnitudTerremoto < 7):
    print("Muy Fuerte (puede causar daños significativos)")
elif (magnitudTerremoto >= 7):
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad 10 

hemisferio = input("Ingrese N si se encuentra en el hemisferio Norte o S si se encuentra en el hemisferio Sur ").lower()
dia = int(input("Ingrese el día "))
mes = int(input("Ingrese el número de mes "))

if (hemisferio == "n"):
    if (mes == 1 or mes == 2 or mes == 3 and dia < 21 or mes == 12 and dia >= 21):
        print("Es invierno")
    elif (mes == 4 or mes == 5 or mes == 6 and dia < 21 or mes == 3 and dia >= 21):
        print("Es primavera")
    elif (mes == 7 or mes == 8 or mes == 9 and dia < 21 or mes == 6 and dia >= 21):
        print("Es verano")
    elif (mes == 10 or mes == 11 or mes == 12 and dia < 21 or mes == 9 and dia >= 21):
        print("Es otoño") 

if (hemisferio == "s"):
    if (mes == 1 or mes == 2 or mes == 3 and dia < 21 or mes == 12 and dia >= 21):
        print("Es verano")
    elif (mes == 4 or mes == 5 or mes == 6 and dia < 21 or mes == 3 and dia >= 21):
        print("Es otoño")
    elif (mes == 7 or mes == 8 or mes == 9 and dia < 21 or mes == 6 and dia >= 21):
        print("Es invierno")
    elif (mes == 10 or mes == 11 or mes == 12 and dia < 21 or mes == 9 and dia >= 21):
        print("Es primavera")   