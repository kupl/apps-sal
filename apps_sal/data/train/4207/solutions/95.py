def sum_cubes(n):
    cubes = map(lambda x: x ** 3, range(1, n + 1))    
    return sum(cubes)
