def find_nb(m):
    l = 1
    while m > 0:
        m -= l**3
        l += 1
    return l - 1 if m == 0 else -1
