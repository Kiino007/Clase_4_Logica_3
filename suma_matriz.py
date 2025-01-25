#Ejercicio 2: suma de los elementos de una matriz
#objetivo:

#crear una matriz de 3x3
#Sumar todos sus elementos y mostrar el resultado

matriz = [
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

for i in range(3):
    for j in range(3):
        suma += matriz[i][j]

print(f"La suma de los elementos es: {suma}")