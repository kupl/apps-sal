def shared_bits(a, b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    if len(a) > len(b):
        b = b.zfill(len(a))
    else:
        a = a.zfill(len(b))

    a = list(a)
    b = list(b)

    return [x + y for x, y in zip(a, b)].count('11') > 1
