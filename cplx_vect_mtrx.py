#Adición de vectores complejos.
def sum_vectors(a, b):
    large = len(a)
    result =[0 for i in range (large)]
    for i in range(large):
        result[i] = a[i] + b[i]
    return result

#Inverso (aditivo) de un vector complejos
def inver_vector(a):
    for i in range(len(a)):
        a[i] = -1 * a[i]
    return a

#Multiplicación de un escalar por un vector complejo.
def escalar_vector(a, b):
    for i in range(len(b)):
        b[i] = a * b[i]
    return b

#Adición de matrices complejas.
def sum_matrix(a,b):
    large = len(a)
    width= len(a[0])
    for i in range(large):
        for j in range(width):
            a[i][j] += b[i][j]
    return a

#Inversa (aditiva) de una matriz compleja.
def inver_adit_matrix(a):
    large = len(a)
    width = len(a[0])
    for i in range(large):
        for j in range(width):
            a[i][j] *= -1
    return a

#Multiplicación de un escalar por una matriz compleja.
def esc_mat(a,b):
    large = len(b)
    width = len(b[0])
    for i in range(large):
        for j in range(width):
            b[i][j] *= a
    return b

#Transpuesta de una matriz/vector
def trans_mat_or_vector(a):
    if isinstance(a[0], list):
        transM = [[0 for i in range(len(a[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                transM[j][i] = a[i][j]
    else:
        transM = []
        for i in range(len(a)):
            transM.append([a[i]])

    return transM

#Conjugada de una matriz/vector
def conj_mat_or_vector(a):
    if isinstance(a[0], list):
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j]= a[i][j].conjugate()
    else:
        for i in range(len(a)):
            a[i] = a[i].conjugate()
    return a

#Adjunta (daga) de una matriz/vector
def adjunta(a):
    return trans_mat_or_vector(conj_mat_or_vector(a))
