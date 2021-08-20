def hamming_distance(a, b):
    total = 0
    a = list(bin(a)[2:])
    b = list(bin(b)[2:])
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b.insert(0, '0')
    elif len(b) > len(a):
        for i in range(len(b) - len(a)):
            a.insert(0, '0')
    for index in range(len(a)):
        if a[index] != b[index]:
            total += 1
    return total
