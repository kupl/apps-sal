def square_digits(num):
    s = str(num)
    t = len(s)
    y = 0
    g = 0
    b = ''
    while y < t:
        g = int(s[y]) ** 2
        b = b + str(g)
        final = int(b)
        y = y + 1
    return final
    pass
