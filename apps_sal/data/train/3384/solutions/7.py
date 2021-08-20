def lucas_lehmer(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    s = 4
    mp = 2 ** n - 1
    for i in range(n - 2):
        s = s * s - 2
        while s >= mp:
            s = (s >> n) + (s & mp)
            if s == mp:
                s = 0
    return s == 0
