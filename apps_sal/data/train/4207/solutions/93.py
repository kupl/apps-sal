def sum_cubes(n):
    sums = []
    for item in range(n):
        item += 1
        cube = pow(item, 3)
        sums.append(cube)
    return sum(sums)
