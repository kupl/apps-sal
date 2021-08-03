def powers_of_two(n):
    l = []
    i = 0
    while i <= n:
        l.append(2**i)
        if i <= n:
            i += 1
    return l
