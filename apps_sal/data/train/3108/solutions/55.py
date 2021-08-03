def multi_table(number):
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    b = []
    f = 1
    g = ''
    for i in a:
        f = i * number
        b.append('{e} * {d} = {c}'.format(e=i, d=number, c=f))
        g = "\n".join(b)
    return g
