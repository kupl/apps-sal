def lucas_lehmer(n):
    if n == 2:
        return True
    m = 2 ** n - 1
    s = 4
    for i in range(2, n):
        ss = s * s
        s = (ss >> n) + (ss & m)
        if s >= m:
            s -= m
        s -= 2
    return s == 0
