def sum_cubes(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i ** 3
    return suma


print(sum_cubes(2))
