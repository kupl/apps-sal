def sum_cubes(n):
    tot = 0
    for x in range(1,n+1):
        tot += x **3
    return tot
