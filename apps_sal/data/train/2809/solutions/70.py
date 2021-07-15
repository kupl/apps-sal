def digitize(n):
    s = list(reversed(str(n)))
    a = [];
    for x in s:
        m = int(x)
        a.append(m)
    return a
