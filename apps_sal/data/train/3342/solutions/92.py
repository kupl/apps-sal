def pattern(n):
    z = ''
    for x in range(1, n + 1):
        i = 0
        while i < x:
            z = z + str(x)
            i = i + 1
        if x != n:
            z = z + '\n'
    return z
