def riders(s):
    r = 1
    d = 0
    for i in s:
        d += i
        if d > 100:
            r += 1
            d = i
    return r
