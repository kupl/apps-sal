def seven(m):
    s = str(m)
    i = 0
    while len(s) > 2:
        s = str(int(s[:-1]) - int(s[-1:]) * 2)
        i += 1
    return int(s), i
