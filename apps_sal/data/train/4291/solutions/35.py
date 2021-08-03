def century(year):
    if year < 101:
        m = 1
    else:
        y = str(year)
        m = int(y[:-2])
        n = int(y[-2:])
        if n != 0:
            m += 1
    # print(m)
    return m
