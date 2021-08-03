def seven(m):
    s = str(m)
    for t in range(0, 100):
        if int(s) <= 99:
            return (int(s), t)
        else:
            r = int(s[:-1]) - int(s[-1]) * 2
            s = str(r)
