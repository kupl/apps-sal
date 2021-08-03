def sum_cubes(n):

    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    x = [i**3 for i in arr]
    return sum(x)
