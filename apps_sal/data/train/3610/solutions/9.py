def fixed_xor(a, b):
    l = min(len(a), len(b))
    if not l:
        return ''
    if len(a) != len(b):
        a, b = a[0:l], b[0:l]
    return hex(int(a, 16) ^ int(b, 16))[2:].rjust(l, '0')
