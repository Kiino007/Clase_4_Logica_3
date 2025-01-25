#Matrices 
#Es una estructura bidimensional, que organiza elemento en filas y columnas, esto crea una tabla de datos

#Cada posicion dentro de la matriz esta identificada por 2 indicen: el indice de la fila y el de la columna, 
#esto permite acceder a los datos de una forma rapida y eficiente 

#Simplificando, una matriz es una coleccion de arreglos unidimensionales dispuestos en varias filas

#Como se ve una matriz de 3 x 3 
#Caracteristicas:
#Dimencionalidad: tiene 2 o mas dimensiones, con un numero definido de filas y columnas
#Se puede xtender a mas dimensiones

#Indexacion:
#Cada elemento tiene una ubicacion unica representada por dos indice [fila] [columna]

#Homogeneidad:
#Suelen tener elementos del mismo tipo de datos (enteros, flotantes, caracteres, booleanos)

#Estructura contigua:
#se almacenan en bloqes contiguos de memoria, lo que permite acceeso eficiente a los datos

#Usos mas frecuentes
#usadas en ciencia de datos, graficos de computadora, bases de datos y otras opciones

#Ejemplos practicos de uso de matrices en la vida real...

#Las matrices se suelen usar en una variedad de casos como
#Tablas de datos:
# Almacenar las notas de estudiantes de diferetes materias

#Imagen digital:
#las imagenes son tambien matrices formadas de pixeles, estos pixeles puedes representarse como arreglos 
#de valores de color

#juegos de video
#un ajedrez es una matriz 

#Algoritmos matematicos:
#se usan en algebra lineal, simulaciones y calculos estadicos

#Represetacion de matrices en programacion
#en algunos lenguajes como los compilados no interpretados de tipado fuerte como java o c++, 
#las matrices tienen una estructura rigida donde al principio se deben declarar el tamaño en filas y columnas
#esto es de manera fija. En python las matrices son mas flexibles y se implementan con listas anidadas 

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
print(matriz[0])
print(matriz [1][2])

#como acceder a los elementos de una matriz

#para acceder a ellos oa un elemento especifico usamos sus indicen, el primero SIEMPRE va ser el de la 
#fila(los arreglos interiores) y el segundo SIEMPRE va ser el de las columna(los elementos de los arreglos interiores)

elemento = matriz[2][1]

print(f"elemento {elemento}")

#como se recorren las matrices
#se recorre con un dor dentro de un for

for i in range(len(matriz)): #recorrer las filas
    for j in range(len(matriz[i])):
        print(f"Elemento en la fila {i} en la columna {j} es: {matriz[i][j]}")


#puedo modificar valores en la matriz
#podemos cambiar un valor aceddiendo directamente por la posicion 
        
matriz[1][1] = 99
print(f"la matriz ha quedado asi: {matriz}")

#operaciones comunes con matrices
#algunas operaciones importantes que se pueden realizar sobre matrices incluyen:

#llenado de matrices con datos del usuario
#suma de elementos de la matriz
#busqueda de un elemento especifico
#transposicion de la matriz (intercambio de filas por columnas) 