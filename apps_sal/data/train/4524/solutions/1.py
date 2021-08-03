def permutation_average(n):
    n = str(n)
    n, l = sum(map(int, n)) / float(len(n)), len(n)

    n = n * ((10 ** l - 1) / 9)

    return round(n)
