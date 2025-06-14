# Actividad 1

def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)
    
factorial_recursivo(int(input("Por favor ingrese un número entero positivo: ")))

# Actividad 2

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)

posicion = int(input("Por favor ingrese la posición cuyo valor desea calcular: "))

for i in range(posicion+1):
    print (f"Posición: {i} Valor fibonacci: {fibonacci_recursivo(i)}")

# Actividad 3

def potencia_recursiva(num,exponente):
    if exponente == 0:
        return 1
    else: 
        return num * potencia_recursiva(num,exponente-1)

base = int(input("Por favor ingrese el número base: "))  
exponente = int(input("Por favor ingrese el exponente: "))  
potencia_recursiva(base,exponente)

# Actividad 4

def binario_recursivo(num):
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    return binario_recursivo(num // 2) + str(num % 2)

numero = int(input("Por favor ingrese el número que desea convertir a binario: "))
binario_recursivo(numero)

# Actividad 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return "Es palíndromo"
    if palabra[0] != palabra[-1]:
        return "NO es palíndromo"
    return es_palindromo(palabra[1:-1])

es_palindromo(input("Ingrese una palabra: "))

# Actividad 6

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        digito = n % 10
        suma = 0
        suma += digito
    return suma + suma_digitos(n // 10)

n = int(input("Por favor ingrese un número: "))
suma_digitos(n)

# Actividad 7

def contar_bloques(n):
    bloques = n
    if n == 1:
        return 1
    else:
        nivel = n
        bloques += n
    return nivel + contar_bloques(n-1)

n = int(input("Por favor ingrese la cantidad base de bloques: "))
contar_bloques(n)

# Actividad 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
numero = int(input("Por favor ingrese el número: "))
digito = int(input("Por favor ingrese el digito: "))

print(contar_digito(numero,digito))

