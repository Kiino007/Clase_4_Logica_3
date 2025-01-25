#Ejercicio 3: buscar un elemento en la matriz
#objetivo:

#Solicitar al usuario una matriz 3x3
#pedir un numero y verificar si se encuentra en la matriz

matriz = []

for i in range(3):
    fila =[]
    for j in range(3):
        valor = int(input("ingrese el valor para la posicion [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

buscar = int(input("Ingrese el numero que va buscar: "))
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == buscar:
            print(f"el numero {buscar} se encuentra en la posicion [{i}][{j}]")
            encontrado = True

if not encontrado:
    print("el numero no se encuentra en la matriz")