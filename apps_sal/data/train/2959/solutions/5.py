def optimal_number_of_coins(n, A):
    D = {}
    for i in range(1, n + 1):
        D[i] = min((j + (i - j * x and D[i - j * x]) for x in set(A) for j in range(1, i // x + 1)))
    return D[n]
