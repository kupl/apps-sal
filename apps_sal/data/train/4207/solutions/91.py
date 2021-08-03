def sum_cubes(n):
    cubed = 0
    for i in range(n + 1):
        cubed += i * i * i
        i += 1
    return cubed
