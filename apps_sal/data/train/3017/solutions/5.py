def rocks(n):
    tot = 0
    for i in range(10):
        if n >= 10**(i + 1):
            tot += 9 * (i + 1) * 10**i
        else:
            tot += (1 + n - 10**i) * (i + 1)
            break
    return tot
