def to_twos_complement(b, bits):
    b = b.replace(" ", "")
    return int(b, 2) if int(b, 2) < 2**(bits - 1) else int(b, 2) - 2**(bits)


def from_twos_complement(n, bits):
    return bin(2**bits + n)[2:].zfill(bits) if n < 0 else bin(n)[2:].zfill(bits)
