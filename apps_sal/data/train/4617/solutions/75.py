def powers_of_two(n):
    x = [1]
    if n == 0:
        return x
    else:
        for i in range(1, n + 1):
            x.append(2**i)
    return x
