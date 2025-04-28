# Muestra un menú para que el usuario elija una compuerta lógica
def menu():
    print("\n--- Seleccione una Compuerta Lógica ---")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. NAND")
    print("5. NOR")
    print("6. XOR")
    print("7. XNOR")
    print("8. Salir")
    opcion = int(input("Ingrese el número de la compuerta lógica que desea usar: "))
    return opcion

# Pide al usuario que ingrese un valor booleano (0 o 1), y valida que sea correcto
def pedir_booleano():
    numero = int(input("Ingrese un dato (0 o 1): "))
    while numero != 0 and numero != 1:
        print("Error: dato inválido.")
        numero = int(input("Ingrese un dato nuevo (0 o 1): "))
    return numero

# Compuerta lógica AND: devuelve 1 solo si ambos valores son 1
def compuerta_and(a, b):
    return int(a and b)

# Compuerta lógica OR: devuelve 1 si al menos uno de los valores es 1
def compuerta_or(a, b):
    return int(a or b)

# Compuerta lógica NOT: invierte el valor (0 → 1, 1 → 0)
def compuerta_not(a):
    return int(not a)

# Compuerta lógica NAND: es lo opuesto de AND
def compuerta_nand(a, b):
    return int(not (a and b))

# Compuerta lógica NOR: es lo opuesto de OR
def compuerta_nor(a, b):
    return int(not (a or b))

# Compuerta lógica XOR: devuelve 1 solo si los valores son distintos
def compuerta_xor(a, b):
    return int(a ^ b)

# Compuerta lógica XNOR: devuelve 1 solo si los valores son iguales
def compuerta_xnor(a, b):
    return int(not (a ^ b))

# Función principal que maneja el menú y la ejecución de las compuertas
def main():
    opcion = menu()  # Mostrar el menú y guardar la opción elegida
    while opcion != 8:  # Mientras no se elija "Salir"
        if opcion != 3:
            # Si no es NOT, se piden dos valores (a y b)
            a = pedir_booleano()
            b = pedir_booleano()
        else:
            # Si es NOT, solo se pide un valor (a)
            a = pedir_booleano()

        # Según la opción elegida, se ejecuta la operación lógica correspondiente
        if opcion == 1:
            print(f"{a} AND {b} = {compuerta_and(a, b)}")
        elif opcion == 2:
            print(f"{a} OR {b} = {compuerta_or(a, b)}")
        elif opcion == 3:
            print(f"NOT {a} = {compuerta_not(a)}")
        elif opcion == 4:
            print(f"{a} NAND {b} = {compuerta_nand(a, b)}")
        elif opcion == 5:
            print(f"{a} NOR {b} = {compuerta_nor(a, b)}")
        elif opcion == 6:
            print(f"{a} XOR {b} = {compuerta_xor(a, b)}")
        elif opcion == 7:
            print(f"{a} XNOR {b} = {compuerta_xnor(a, b)}")
        else:
            print("Opción inválida.")

        opcion = menu()  # Mostrar el menú nuevamente para seguir operando

# Inicia el programa
main()