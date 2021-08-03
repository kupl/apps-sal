def halving_sum(n):
    i = 0
    x = 0
    while True:
        if n // 2 ** i > 0:
            x = x + n // 2 ** i
            i = i + 1
        else:
            break
    return x
