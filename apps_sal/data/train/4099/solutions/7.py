def flip_bit(value, bit_index):
    bits = list(map(int, bin(value)[2:]))
    while len(bits) < bit_index:
        bits.insert(0, 0)
    bits[len(bits) - bit_index] ^= 1
    return int(''.join(map(str, bits)), 2)
