numero = 10

while numero >= 1:
    print(numero)
    numero = numero - 1

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1

numero = 2

while numero <= 20:
    print(numero)
    numero = numero + 2

respuesta = input("Que desea hacer?")
while respuesta != "salir":
    print("Programa en curso")
    respuesta = input("Que desea hacer?")

while True:
 
    print("SELECCIONE SU RESPUESTA")
    print("1. Saludar")
    print("2. Decir que Python es genial")
    print("3. Salir")
    respuesta = input("Que desea hacer?")

    if respuesta == "1":
            print("Hola mundo")

    elif respuesta == "2":
            print("Python es genial")
    elif respuesta == "3":
            print("FINALIZANDO PROGRAMA")
            break
    else:
         print("Opción inválida")

while True:
    numero = int(input("SELECCIONE UN NUMERO ENTERO:"))
    if numero < 0:
         continue
    if numero == 0:
         break
    print(numero)

contraseña = "python123"
intentos = 0

while intentos < 3:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña:
        print("Acceso concedido.")
        break
    else:
         intentos = intentos + 1
         print("Contraseña incorrecta. ")
if intentos == 3:
    print("Demasiados intentos")