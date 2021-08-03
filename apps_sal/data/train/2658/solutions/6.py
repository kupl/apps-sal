def binary(x): return bin(x)[2:].zfill(32)


def convert_bits(a, b):
    a, b = binary(a), binary(b)
    return sum(a[i] != b[i] for i in range(32))
