def i2l(i):
    l = []
    while i != 0:
        l.append(i % 2)
        i >>= 1
    l.reverse()
    return l if l else [0]


def l2i(l):
    i = 0
    for b in l:
        i = i * 2 + b
    return i


def bin2gray(bits):
    bits = l2i(bits)
    return i2l(bits ^ bits >> 1)


def gray2bin(bits):
    bits = l2i(bits)
    m = bits >> 1
    while m:
        bits = bits ^ m
        m >>= 1
    return i2l(bits)
