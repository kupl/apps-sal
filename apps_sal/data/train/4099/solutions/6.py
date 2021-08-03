def flip_bit(value, bit_index):
    bs = list(bin(value)[2:].zfill(bit_index))
    i = len(bs) - bit_index
    bs[i] = '10'[int(bs[i])]
    return int(''.join(bs), 2)
