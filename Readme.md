# Libreria números complejos parte 2.

## Esta libreria trabaja sobre algunas operaciones sobre vectores y matrices con números complejos

1. Adición de vectores complejos.

Para esta función se crea un vector de ceros mediante una lista indexada con el fin de guardar el resultado de la suma de los vectores(result).
Se parte del hecho que los vectores tienen misma longitud.
```python
def sum_vectors(a, b):
    large = len(a)
    result =[0 for i in range (large)]
    for i in range(large):
        result[i] = a[i] + b[i]
    return result
```

2. Inverso (aditivo) de un vector complejos.

Para esta función tenga en cuenta que la entrada si o si tiene que se un vector.
```python
def inver_vector(a):
    for i in range(len(a)):
        a[i] = -1 * a[i]
    return a
```

3. Multiplicación de un escalar por un vector complejo.

No detalles.

4. Adición de matrices complejas.

No se emplea una matriz adicional de resultados ya que en el proceso iterativo no se almacena en una variable.
```python
def sum_matrix(a,b):
    large = len(a)
    width= len(a[0])
    for i in range(large):
        for j in range(width):
            a[i][j] += b[i][j]
    return a
```

5. Inversa (aditiva) de una matriz compleja.


```python
def inver_adit_matrix(a):
    large = len(a)
    width = len(a[0])
    for i in range(large):
        for j in range(width):
            a[i][j] *= -1
    return a
```
6. Multiplicación de un escalar por una matriz compleja.

No detalles.

7. Transpuesta de una matriz/vector

Observe como en el fragmento de código se genera una especie de matriz para un vector
la intención de esto es a la hora de imprimer se visualice de forma de vector columna.
```python
    else:
        transM = []
        for i in range(len(a)):
            transM.append([a[i]])
    return transM
```

8. Conjugada de una matriz/vector

Para esta función aplicamos el método conjugate
```python
def conj_mat_or_vector(a):
    if isinstance(a[0], list):
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j]= a[i][j].conjugate()
    else:
        for i in range(len(a)):
            a[i] = a[i].conjugate()
    return a
```

