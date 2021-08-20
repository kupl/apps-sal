def powers_of_two(n):
    emptylist = []
    for i in range(n + 1):
        x = 2 ** i
        emptylist.append(x)
    return emptylist
