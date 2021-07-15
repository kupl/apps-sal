def basereduct(x):
    limit = x * 1000000
    while x >= 10 and x <= limit:
        s = str(x)
        base = int(max(s)) + 1
        x = int(s, 11 if base == 10 else base)
    return x if x < 10 else -1
