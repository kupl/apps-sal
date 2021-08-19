def powers_of_two(n):
    a = 2
    b = []
    for i in range(n + 1):
        b.append(2 ** i)
    return b
