def seven(m):
    s = 0
    if m < 100:
        s = 0
    else:
        while m > 99:
            x = m // 10
            m = str(m)
            y = int(m[-1])
            m = x - 2 * y
            s = s + 1

    return((m, s))
