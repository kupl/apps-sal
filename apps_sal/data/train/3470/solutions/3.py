def to_twos_complement(binary, bits):
    return int(binary.replace(' ', ''), 2) - 2 ** bits * binary.startswith('1')


def from_twos_complement(n, bits):
    return '{:0{}b}'.format((n + 2 ** bits) % 2 ** bits, bits)
