def fixed_xor(a, b):
    l = min(len(a), len(b))
    r = '' if not a[:l] else hex(int(a[:l], 16) ^ int(b[:l], 16))[2:]
    return '0' * (l - len(r)) + r
