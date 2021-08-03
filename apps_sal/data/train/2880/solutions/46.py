def seven(m):
    n = m
    s = str(n)
    cnt = 0
    while len(s) > 2:
        n = int(s[:-1]) - int(s[-1]) * 2
        s = str(n)
        cnt += 1
    return (int(s), cnt)
