def powers_of_two(n):
    d, a = [], 1
    for i in range(n + 1):
        d.append(a)
        a *= 2
    return d
