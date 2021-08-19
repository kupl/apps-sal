def basereduct(x):
    count = 0
    while len(str(x)) > 1:
        base = max((int(i) for i in str(x)))
        if base == 9:
            x = int(str(x), 11)
        else:
            x = int(str(x), base + 1)
        count += 1
        if count >= 150:
            return -1
    return x
