def sum_cubes(n):
    sums = 0
    for num in range(0, n+1):
        sums+= (num **3)
    return sums
