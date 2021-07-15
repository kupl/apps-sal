def arbitrate(input, n):
    return '{:0{}b}'.format(2 ** int(input, 2).bit_length() // 2, n)
