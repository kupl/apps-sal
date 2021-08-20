def permutation_average(n):
    n = str(n)
    avg = sum(map(int, n)) / len(n)
    return round(avg * int('1' * len(n)))
