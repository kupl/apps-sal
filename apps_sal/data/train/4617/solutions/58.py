def powers_of_two(n):
    newN = []
    num = 0
    while num <= n:
        newN += [2 ** num]
        num += 1
    return newN
