def powers_of_two(n):
    lst = []
    for i in range(0, n + 1):
        lst.append(i)
    return list(map(lambda x: 2 ** x, lst))
