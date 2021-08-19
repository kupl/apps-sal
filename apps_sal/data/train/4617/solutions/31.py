def powers_of_two(n):
    i = 0
    list = [1]
    for i in range(1, n + 1):
        list += [2 ** i]
    return list
