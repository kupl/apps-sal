def powers_of_two(n):
    return [2 ** i if i != 0 else 1 for i in range(0, n + 1)]
