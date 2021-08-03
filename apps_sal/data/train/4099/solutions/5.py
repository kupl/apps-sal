def flip_bit(v, i):
    v = list(bin(v)[2:].rjust(i, "0")[::-1])
    v[i - 1] = str(1 - int(v[i - 1]))
    return int("".join(v[::-1]), 2)
