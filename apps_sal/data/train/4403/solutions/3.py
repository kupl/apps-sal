# Python 3 rocks!
def switch_endian(n, bits): return int.from_bytes(n.to_bytes(bits // 8, 'big'), 'little') if bits % 8 == 0 and bits >= 8 and n.bit_length() <= bits else None
