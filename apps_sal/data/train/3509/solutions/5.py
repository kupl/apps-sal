def meters(x):
    s = ['m', 'km', 'Mm', 'Gm', 'Tm', 'Pm', 'Em', 'Zm', 'Ym']
    i = 0
    while x >= 1000:
        x /= 1000.0
        i += 1
    return '%g%s' % (x, s[i])
