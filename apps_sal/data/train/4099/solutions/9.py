def flip_bit(v, b):
    k = list(bin(v)[2:].zfill(b))
    k[-b] = str(1 - int(k[-b]))
    return int(''.join(k), 2)
