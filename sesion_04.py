edad = int(input("Ingrese su edad:"))

if edad >= 18:
    print("Adulto")

elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")

nota = float(input("Ingrese su nota:"))

if nota >= 0.0 and nota <= 5.0:
    if nota >= 4.5:
       print("Excelente")

    elif nota >= 4.0:
       print("Muy bien")

    elif nota >= 3.5:
       print("Aprobado")
    
    else:
       print("No aprobado")
else:
    print("Nota inválida")
    
edad = int(input("Ingrese su edad:"))
dinero_disponible = int(input("Ingrese su dinero disponible:"))
tiene_membresia = input("¿Tiene membresía?(si/no):")

if edad >= 18:

    if dinero_disponible >= 100000:
        print("Puede comprar")

    elif dinero_disponible >= 50000 and tiene_membresia == "si":
        print("Compra aprobada con beneficio de membresía")

    else:
        print("Fondos insuficientes")

else:
    print("No puede comprar")

nivel = int(input("Ingrese su nivel:"))
llave_especial = input("¿Tiene la llave especial?(si/no):")

if nivel >= 50 or llave_especial == "si":
    print("Puede entrar")

else:
    print("No puede entrar")

nota = float(input("Ingrese su nota:"))

if nota < 0.0 or nota > 5.0:
    print("Nota inválida")

else:
    if nota >= 4.5:
        print("Excelente")

    elif nota >= 4.0:
        print("Muy bien")

    elif nota >= 3.5:
        print("Aprobado")

    else:
        print("No aprobado")