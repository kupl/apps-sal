def switch_endian(n, bits):
    if n < 0 or bits & (bits - 1) or bits < 8 or n >= 2**bits:
        return None
    result = 0
    for _ in range(bits // 8):
        result = (result << 8) | (n & 255)
        n >>= 8
    return result
