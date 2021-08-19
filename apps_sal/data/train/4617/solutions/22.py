def powers_of_two(n):
    s = []
    for el in range(0, n + 1):
        s.append(2 ** el)
    return s
