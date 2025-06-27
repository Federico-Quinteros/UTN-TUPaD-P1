# Actividad 1
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Actividad 2
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Actividad 3
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Actividad 4
agenda = {}

print("Cargar contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

print("Consultar número:")
nombre_busqueda = input("Ingrese el nombre del contacto que desea buscar: ")

if nombre_busqueda in agenda:
    print(f"El número de {nombre_busqueda} es: {agenda[nombre_busqueda]}")
else:
    print(f"{nombre_busqueda} no está en la agenda.")

# Actividad 5
frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Palabras únicas:")
print(palabras_unicas)

print("Frecuencia de palabras:")
for palabra, cantidad in frecuencia_palabras.items():
    print(f"{palabra}: {cantidad}")

# Actividad 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    notas = tuple(int(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    
    alumnos[nombre] = notas

print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Actividad 7
parcial1 = {"Juan", "Fede", "Agos", "Tomi", "Cami"}
parcial2 = {"Fede", "Tomi", "Cami","Rocio"}

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("Estudiantes que aprobaron ambos parciales:")
print(ambos)
print("Estudiantes que aprobaron solo uno de los dos:")
print(solo_uno)
print("Total de estudiantes que aprobaron al menos un parcial:")
print(al_menos_uno)

# Actividad 8
stock_productos = {
    'arroz': 10,
    'fideos': 20,
    'harina': 15
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    
    agregar = input("¿Desea agregar unidades? (s/n): ").lower()
    if agregar == 's':
        unidades = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
    else:
        print("No se realizaron cambios.")
else:
    print(f"{producto} no está en el inventario.")
    agregar_nuevo = input("¿Desea agregarlo como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == 's':
        unidades = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] = unidades
        print(f"{producto} fue agregado con {unidades} unidades.")
    else:
        print("Producto no agregado.")

print("Stock actual:")
for nombre, cantidad in stock_productos.items():
    print(f"{nombre}: {cantidad}")

# Actividad 9
agenda = {
    ('lunes', '10:00'): 'Dentista',
    ('martes', '14:30'): 'Siesta',
    ('miércoles', '08:00'): 'Gimnasio',
    ('viernes', '18:00'): 'Partido de basquet'
}

dia = input("Ingrese el día (por ejemplo: lunes): ").lower()
hora = input("Ingrese la hora (por ejemplo: 14:30): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad el {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay actividad registrada para el {dia} a las {hora}.")

# Actividad 10
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital → país):")
print(capitales_paises)