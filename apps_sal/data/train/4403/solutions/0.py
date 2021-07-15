def switch_endian(n, bits):
    out = 0
    while bits > 7:
        bits -= 8
        out <<= 8
        out  |= n & 255
        n   >>= 8
    return None if n or bits else out
