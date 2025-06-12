# Actividad 1
def imprimir_mensaje(mensaje):
    return print(mensaje)

imprimir_mensaje("Hola Mundo")

# Actividad 2
def saludar_usuario(nombre):
    return print(f"Hola {nombre}")

saludar_usuario(input("Ingrese su nombre: "))

# Actividad 3
def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "),input("Ingrese su edad: "),input("Ingrese su lugar de residencia: "))

# Actividad 4
def calcular_area_circulo(radio):
    area_circulo = 3.14 * radio **2
    return print(f"El área del circulo es {area_circulo} cm2")

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * 3.14 * radio
    return print(f"El perímetro del circulo es {perimetro_circulo} cm")

calcular_area_circulo(int(input("Ingrese el radio del circulo: ")))
calcular_perimetro_circulo(int(input("Ingrese el radio del circulo: ")))

# Actividad 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(f"{segundos} segundos corresponden a {horas} horas!")

segundos_a_horas(int(input("Ingrese la cantidad de segundos: ")))

# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print (f"{numero} x {i} = {resultado}")
     
    
tabla_multiplicar(int(input("Ingrese un número: ")))

# Actividad 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} * {b} = {multiplicacion}")
    print(f"{a} / {b} = {division}")

operaciones_basicas(int(input("Ingrese el primer número: ")),int(input("Ingrese el segundo número: ")))

# Actividad 8
def calcular_imc(peso, altura):
    imc = peso / altura**2
    print(f"Su IMC es igual a {imc}")

calcular_imc(float(input("Ingrese su peso en kg: ")),float(input("Ingrese su altura en mt: ")))

# Actividad 9
def celsius_a_fahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados celsius equivalen a {farenheit} grados farenheit.")

celsius_a_fahrenheit(float(input("Ingrese la temperatura en grados celsius: ")))

# Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los números ingresados es igual a {promedio}")

calcular_promedio(int(input("Ingrese el primer número: ")),int(input("Ingrese el segundo número: ")),int(input("Ingrese el tercer número: ")))
