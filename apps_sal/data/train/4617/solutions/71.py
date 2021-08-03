
def powers_of_two(n):
    return list(map(lambda x: 2**(x - 1), list(range(1, n + 2))))
