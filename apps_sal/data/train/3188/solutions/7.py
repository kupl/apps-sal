def basereduct(x):
    count = 0
    while x >= 10:
        if count == 150:
            return -1
        s = str(x)
        b = max(map(int, s)) + 1
        if b == 10:
            b, count = 11, count + 1
        x = int(s, b)
    return x
