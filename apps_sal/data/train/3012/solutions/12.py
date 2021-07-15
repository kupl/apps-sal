def shared_bits(a, b):
    a = bin(a)
    b = bin(b)
    n = 0
    for i in range(1, min(len(a), len(b))):
        if a[-i] == b[-i] and a[-i] == '1':
            n += 1
    return n >= 2
