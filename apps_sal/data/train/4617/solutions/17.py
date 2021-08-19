def powers_of_two(n):
    x = []
    while n > -1:
        y = 2 ** n
        x.append(y)
        n = n - 1
    return x[::-1]
