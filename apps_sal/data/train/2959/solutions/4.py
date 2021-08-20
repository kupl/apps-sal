def optimal_number_of_coins(n, A):
    D = {}
    for i in range(1, n + 1):
        D[i] = min((-~j + (i + ~j * x and D[i + ~j * x]) for x in A for j in range(i // x)))
    return D[n]
