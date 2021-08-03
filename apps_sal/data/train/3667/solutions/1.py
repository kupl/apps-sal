def mid_endian(n):
    bs = n.to_bytes((n.bit_length() + 7) // 8 or 1, byteorder='little')
    return (bs[len(bs) % 2::2] + bs[::-2]).hex().upper()
