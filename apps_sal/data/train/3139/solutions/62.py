def index(array, n):
    contar = 0
    for numero in array:
        contar = contar + 1
    if contar > n:
        y = array[n]
        x = y ** n
        return x
    else:
        return -1
