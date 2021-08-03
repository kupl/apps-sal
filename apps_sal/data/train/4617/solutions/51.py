def powers_of_two(n):
    lst = []
    x = 0

    for i in range(0, n + 1):
        x = 2 ** i
        lst.append(x)
    return lst
