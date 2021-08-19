def seven(m, n=0):
    while m > 99:
        n += 1
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
    return (m, n)
