def find(n):
    multsf = [5 * i for i in range(1, n + 1) if 5 * i <= n]
    multst = [3 * i for i in range(1, n + 1) if 3 * i <= n]

    return sum(multst) + sum(list(set(multsf) - set(multst)))
