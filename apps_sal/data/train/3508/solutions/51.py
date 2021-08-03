def halving_sum(n):
    a = [n]
    b = n
    while n > 1:
        c = n // 2
        a.append(c)
        b += c
        n = c
    return b
