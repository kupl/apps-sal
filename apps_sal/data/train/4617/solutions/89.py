def powers_of_two(n):
    new_n = []
    for i in range(n + 1):
        new_n.append(2**i)
    return new_n
