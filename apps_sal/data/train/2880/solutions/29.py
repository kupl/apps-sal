def seven(m, i=0):
    m = str(m)
    n, d = m[:-1], m[-1]

    while len(m) > 2:
        i += 1
        return seven(int(n) - int(d) * 2, i)

    return (int(m), i)
