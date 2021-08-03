def fib_rabbits(n, b):
    table = [0 if i != 1 else 1 for i in range(0, n + 1)]

    for i in range(2, n + 1):
        table[i] = (table[i - 1] + table[i - 2] * b)

    return table[n]
