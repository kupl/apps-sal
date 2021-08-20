def fixed_xor(a, b):
    l = min(len(a), len(b))
    if not l:
        return ''
    (a, b) = (int(a[:l], 16), int(b[:l], 16))
    return hex(a ^ b)[2:].rjust(l, '0')
