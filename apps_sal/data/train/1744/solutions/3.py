def fusc(n):
    (x, y) = (1, 0)
    for i in bin(n)[2:]:
        if i == '1':
            y += x
        else:
            x += y
    return y
