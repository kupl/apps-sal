def multiply(n):
    c = 0
    if n < 0:
        c = c - n
        m = str(c)
    else:
        m = str(n)

    return n * 5**len(m)
