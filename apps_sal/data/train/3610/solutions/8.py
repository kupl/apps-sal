def fixed_xor(a, b):
    return ''.join(('%x' % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a, b)))
