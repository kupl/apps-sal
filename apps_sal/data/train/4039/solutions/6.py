def to_base(x, b):
    r = ''
    while x:
        x, d = divmod(x, b)
        r = f"{d if d<10 else 'x'}" + r
    return r


def fouriest(i):
    best, base = 0, 1
    for b in range(2, i):
        x = to_base(i, b)
        if x.count('4') > best:
            best, base = x.count('4'), b
        if b**best >= i:
            break
    return f"{i} is the fouriest ({to_base(i,base)}) in base {base}"
