def encode(m, key):
    k = list(map(int, list(str(key))))
    kL = len(k)
    m = list(m)
    for i in range(len(m)):
        m[i] = ord(m[i]) - 96 + k[i % kL]
    return m
