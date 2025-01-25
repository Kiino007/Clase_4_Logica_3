#ejercicio 1: creacion d una matriz dinamica
#objetivo:

#pedir al usuario el tamaño de la matriz
#llenarla con valores ingresados manualmente
#imprimir la matriz resultante

filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posicion [{i}][{j}]"))
        fila.append(fila)

    print("matriz ingresada: ")
    for fila in matriz:
        print(fila)
        