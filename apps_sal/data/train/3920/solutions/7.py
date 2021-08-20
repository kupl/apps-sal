def hamming_distance(a, b):
    c = ''
    d = ''
    c = bin(a)[2:]
    d = bin(b)[2:]
    for i in range(32 - len(c)):
        c = '0' + c
    for i in range(32 - len(d)):
        d = '0' + d
    count = 0
    for i in range(32):
        if c[i] != d[i]:
            count += 1
    return count
