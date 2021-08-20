def ips_between(start, end):
    x = []
    x = start.split('.')
    y = []
    u = []
    y = end.split('.')
    for i in range(4):
        u.append(int(y[i]) - int(x[i]))
    t = u[-1]
    for i in range(1, 4):
        t += u[-1 - i] * 256 ** i
    return t
