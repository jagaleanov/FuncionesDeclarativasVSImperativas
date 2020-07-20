# Función que recibe un entero y retorna su factorial.
def factorial ( n ) :
    if n == 0 :
        return 1
    else:
        return n * factorial ( n - 1 )

#print("factorial de 7 ")
#print(factorial ( 7 ))

# Función que recibe un entero y retorna su cuadrado.    
def cuadrado ( n ) :
    return n * n

#print("cuadrado de 7 ")
#print(cuadrado ( 7 ))

# Función retorna una suma infinita de unos.
def infinito () :
    return infinito + 1

# Función que recibe un entero y retorna 3.
def tres ( n ) :
    if n == 3 :
        return n
    elif n > 3 :
        return tres ( n - 1 )
    else :
        return tres ( n + 1 )

#print("tres de 7 ")
#print(tres ( 7 ))

# Función que recibe una lista de enteros y retorna su total.
def sumar ( lista ) :
    if len( lista ) == 1:
        return lista [ 0 ]
    else:
        return lista [ 0 ] + sumar ( lista [ 1 : len ( lista ) ] )

#print("sumar  [1,10,100,1000] ")
#print(sumar ( [1,10,100,1000] ))

# Función que recibe una lista de cualquier tipo de dato y retorna la misma lista en orden inverso.
def invertir ( lista ) :
    if len( lista ) == 1 :
        return lista
    else:
        return invertir( lista [ 1: ] )  + [lista [ 0 ]]

#print("invertir  [1,10,100,1000] ")
#print(invertir ( [1,10,100,1000] ))

# Función que recibe dos listas y compara si son iguales.
def igualLista ( lista1 , lista2 ) :

    if len(lista1) == 0 :
        if len(lista2)==0 :
            return True
        else:
            return False
    else :
        if lista1 [ 0 ] == lista2 [ 0 ] and len(lista1) == len(lista2) :
            return igualLista ( lista1 [ 1: ] , lista2 [ 1: ] )
        else:
            return False

#print("igualLista  [1,10,100,1000] y [1,10,100,1000] ")
#print(igualLista ( [1,10,100,1000] , [1,10,100,1000] ))

# Función que recibe una lista de enteros y retorna el menor.
def menor ( lista ) :
    if len ( lista ) == 1 :
        return lista [ 0 ]
    else:
        if lista [ 0 ] <= lista[ len ( lista )-1 ] :
            return  menor(lista[ : len ( lista )-2 ])
        elif lista [ 0 ] > lista[ len ( lista )-1 ] :
            return  menor(lista[ 1: ])

#print("menor  [10,1000,4,100,84,654,9] ")
#print(menor ( [10,1000,4,100,84,654,9] ))     

# Función que recibe una lista de cualquier tipo de dato y verifica si esta ordenada.
def listaOrdenada ( lista ) :
    if len ( lista ) == 0 :
        return True
    elif len ( lista ) == 1:
        return True
    else:
        if lista [ 0 ] >= lista [ 1 ]:
            return  listaOrdenada ( lista [ 1: ] )
        else:
            return  False

#print("listaOrdenada  [10,1000,4,100,84,654,9] ")
#print(listaOrdenada ( [10,1000,4,100,84,654,9] ))

# Función que recibe una lista de cualquier tipo de dato y un entero y devuelve el valor de la lista en la posicion indicada por el entero.
def mostrarUbicacion ( lista , n ,m=0) :
    if n == m :
        return lista[m]
    elif n > m:
        return  mostrarUbicacion (lista,n,m+1)

#print("mostrarUbicacion 3 en la lista [10,1000,4,100,84,654,9] ")
#print(mostrarUbicacion ( [10,1000,4,100,84,654,9] , 3))      

# Función que recibe una lista de enteros y retorna el mayor.
def mayor ( lista ) :
    if len ( lista ) == 0 :
        return None
    elif len ( lista ) == 1 :
        return lista [ 0 ]
    else:
        if lista [ 0 ] > mayor ( lista [ 1: ]) :
            return lista [ 0 ]
        else :
            return  mayor ( lista [ 1: ] ) 

#print("mayor en la lista [10,1000,4,100,84,654,9] ")
#print(mayor ( [10,1000,4,100,84,654,9] ))  

# Función que recibe una lista de enteros y retorna el conteo de números pares.
def contarPares ( lista ) :
    if len ( lista ) == 1 :
        if lista [ 0 ] % 2 == 0 : 
            return 1
        else : 
            return 0
    else :
        if lista [ 0 ] % 2 == 0 : 
            c = 1
        else : 
            c = 0
        return c + contarPares ( lista [ 1: ] )

#print("mcontarPares en [10,1000,4,100,84,654,9] ")
#print(contarPares ( [10,1000,4,100,84,654,9] ))  

# Función que recibe una lista de enteros y retorna una lista de cuadrados.
def cuadradoLista (lista):
    if len ( lista ) == 1 :
        return [lista [ 0 ] * lista [ 0 ]]
    else:
        return [lista [ 0 ] * lista [ 0 ]] + cuadradoLista (lista [ 1: ])

#print("cuadradoLista de [10,1000,4,100,84,654,9] ")
#print(cuadradoLista ( [10,1000,4,100,84,654,9] ))  

# Función que recibe dos enteros X y Y y retorna si X es divisible en Y.

def divisible (x,y):
    if x < y:
        if x == 0:
            return True
        else:
            return False
    else:
        return divisible(x-y,y)

#print("divisible 28 entre 3 ")
#print(divisible ( 28,3 )) 

# Función que recibe un entero y retorna una lista de numeros que dividen a x.
def divisores (x,y=1):
    if x == 0 :
        return [0]
    elif x == 1:
        return [1]
    elif x == y :
        return [x]
    elif x % y == 0 :
        return divisores (x,y+1)+ [y]
    else:
        return divisores (x,y+1)

#print("divisores de 72 ")
#print(divisores ( 72 )) 

# Función que recibe un entero y retorna si es primo.
def esPrimo (x):
    if len(divisores(x)) == 2:
        return True
    else:
        return False

#print("esPrimo 73 ")
#print(esPrimo ( 73 )) 

# Función que recibe un entero n y retorna una lista de primos menores o igual a n.
def primos (x):
    if x == 0 :
        return []
    elif x == 1 :
        return [1]
    elif esPrimo (x) == True:
        return primos (x-1) + [x]
    else: 
        return primos (x-1)

#print("primos hasta 73 ")
#print(primos ( 73 )) 