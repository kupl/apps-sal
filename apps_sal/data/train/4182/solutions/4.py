def survivor(m):
    i = 2
    while i <= m:
        q, r = divmod(m, i)
        if r == 0:
            return False
        m, i = m - q, i + 1
    return True
