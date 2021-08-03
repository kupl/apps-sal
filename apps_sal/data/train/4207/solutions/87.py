def sum_cubes(n):
    # your code here
    suma = 0
    for i in range(n):
        suma = suma + (i + 1)**3
    return suma
