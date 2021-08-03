def fixed_xor(a, b):
    if not a or not b:
        return ''
    m1 = min(len(a), len(b))
    a, b = bin(int(a[:m1], 16))[2:], bin(int(b[:m1], 16))[2:]
    m = max(len(a), len(b))
    return hex(int("".join([str(int(i) ^ int(j)) for i, j in zip(a.zfill(m), b.zfill(m))]), 2))[2:].zfill(m1)
