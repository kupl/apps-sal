def basereduct(n):
    for _ in range(150):
        b = int(max(str(n))) + 1
        n = int(str(n), 11 if b == 10 else b)
        if n < 10:
            return n
    return -1
