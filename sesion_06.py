for numero in range(5, 11):
    print(numero)

for letra in "Python":
    print(letra)

for palabra in ["Sol", "Casa", "Yo"]:
    print("Palabra actual:", palabra)

    for letra in palabra:
        print(letra)

print("Programa terminado")

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")

suma = 0

for numero in range(1, 11):
    suma = suma + numero
    print("Número:", numero, "- Suma acumulada:", suma)

suma = 0

for numero in range(1, 11):
    suma = suma + numero

print(suma)

suma_par = 0
suma_impar = 0

for numero in range(1, 21):

    if numero % 2 == 0:
        suma_par = suma_par + numero

    else:
        suma_impar = suma_impar + numero

print("Suma de pares:", suma_par)
print("Suma de impares:", suma_impar)

notas = [4.5, 2.8, 3.7, 1.9, 4.2, 3.0]
aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)

notas = [4.5, 2.8, 3.7, 1.9, 4.2, 3.0]
aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados += 1

reprobados = len(notas) - aprobados

print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)

datos = ["Python", "Hola", "Programación"]

print(len(datos))

for palabra in datos:
    print(palabra, len(palabra))

nombres = ["Ana", "Santiago", "Samuel", "Michell"]

print(len(nombres))

for palabra in nombres:
    print(palabra, "tiene", len(palabra), "caracteres")

nombres = ["Ana", "Santiago", "Samuel", "Michell"]

nombres_largos = 0

for palabra in nombres:
    if len(palabra) > 6:
        nombres_largos += 1

print("Nombres con más de 6 caracteres:", nombres_largos)

numeros = [5, 12, 8, 20, 3, 15]

cantidad = 0
suma = 0

for numero in numeros:
    if numero > 10:
        cantidad += 1
        suma += numero

print("Cantidad de números mayores que 10:", cantidad)
print("Suma de los números mayores que 10:", suma)

notas = [4.5, 2.3, 3.8, 1.5, 5.0, 3.0, 2.9, 4.1]

suma_aprobados = 0
suma_reprobados = 0
aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados += 1
        suma_aprobados += nota
    else:
        reprobados += 1
        suma_reprobados += nota

print("Total de aprobados:", aprobados)
print("Total de reprobados:", reprobados)
print("Suma de aprobados:", suma_aprobados)
print("Suma de reprobados:", suma_reprobados)