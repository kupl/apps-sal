def to_twos_complement(input_value, bits):
    mask, unsigned = 2 ** (bits - 1), int(input_value.replace(' ', ''), 2)
    return (unsigned & ~mask) - (unsigned & mask)


def from_twos_complement(n, bits):
    return "{:0>{}b}".format(n + 2 ** bits * (n < 0), bits)
