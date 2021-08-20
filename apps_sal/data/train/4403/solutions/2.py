def switch_endian(n, bits):
    if not (bits >= 8 and bits & bits - 1 == 0 and (bits >= n.bit_length())):
        return None
    return int.from_bytes(n.to_bytes(bits // 8, 'little'), 'big')
