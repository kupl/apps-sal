def basereduct(x):
    c = 0
    while(len(str(x)) > 1):
        b = max(map(int, str(x))) + 1
        if b == 10:
            b = 11
        i = 0
        n = 0
        for d in str(x):
            n = n * b + int(d)
        x = n
        c += 1
        if c > 150:
            return -1
    return x
