seq = (1, 10, 9, 12, 3, 4)


def thirt(n):
    strn = str(n)[::-1]
    m = sum(seq[i % 6] * int(strn[i]) for i in range(len(strn)))
    return n if n == m else thirt(m)
