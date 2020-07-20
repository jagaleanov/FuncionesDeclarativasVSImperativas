-- Función que recibe un entero y retorna su factorial.
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial ( n - 1 )

-- Función que recibe un entero y retorna su cuadrado. 
cuadrado::Int -> Int
cuadrado x = x * x

-- Función retorna una suma infinita de unos.
infinito :: Integer
infinito = 1 + infinito

-- Función que recibe un entero y retorna 3.
tres :: Integer -> Integer
tres x = 3

-- Función que recibe una lista de enteros y retorna su total.
sumar :: [ Int ] -> Int
sumar [ ] = 0
sumar ( x : xs ) = x + sumar( xs )

-- Función que recibe una lista de cualquier tipo de dato y retorna la misma lista en orden inverso.
invertir :: Ord a => [ a ] -> [ a ]
invertir [ ] = [ ]
invertir ( x : xs ) = ( invertir xs ) ++ [ x ]

-- Función que recibe dos listas y compara si son iguales.
igualLista :: Eq a => [ a ] -> [ a ] -> Bool
igualLista l1 l2 = l1 == l2

-- Función que recibe una lista de cualquier tipo de dato y verifica si esta ordenada.
listaOrdenada :: Ord a => [ a ] -> Bool
listaOrdenada [] = True
listaOrdenada [_] = True
listaOrdenada ( x : y : xs ) = ( x <= y ) && listaOrdenada
    ( y : xs )

-- Función que recibe una lista de cualquier tipo de dato y un entero y devuelve el valor de la lista en la posicion indicada por el entero.
mostrarUbicacion :: Ord a => [ a ] -> Int -> a
mostrarUbicacion l n = l !! n

-- Función que recibe una lista de enteros y retorna el mayor.
mayor :: [ Int ] -> Int
mayor ( x : xs )
mayor [x] = x
    | x > mayor ( xs ) = x
    | otherwise = mayor ( xs )

-- Función que recibe una lista de enteros y retorna el conteo de números pares.
contarPares :: [ Int ] -> Int
contarPares [ ] = 0
contarPares lista = length [ x | x <- lista, mod x 2 == 0 ]

-- Función que recibe una lista de enteros y retorna una lista de cuadrados.
cuadrados :: [ Int ] -> [ Int ]
cuadrados [ ] = [ ]
cuadrados l = [ x * x | x <- l ]

-- Función que recibe dos enteros X y Y y retorna si X es divisible en Y.
divisible :: Int -> Int -> Bool
divisible x y = ( mod x y ) ==0

-- Función que recibe un entero y retorna una lista de numeros que dividen a x.
divisores :: Int -> [ Int ]
divisores x = [ y | y <- [1..x], divisible x y ]

-- Función que recibe un entero y retorna si es primo.
esPrimo::Int -> Bool
esPrimo n = length ( divisibles n ) <= 2

-- Función que recibe un entero n y retorna una lista de primos menores o igual a n.
primos :: Int -> [ Int ]
primos n = [ x | x <- [ 1 .. n ], esPrimo x ]
