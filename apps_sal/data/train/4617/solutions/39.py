def powers_of_two(n):
    a = []
    b = 1
    for i in range(0, n + 1):
        a.append(b)
        b = b * 2
    return a
