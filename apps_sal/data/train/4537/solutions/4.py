def bin2gray(bits):
    return bits[:1] + [b1 ^ b2 for (b1, b2) in zip(bits, bits[1:])]


def gray2bin(bits):
    return [reduce(lambda x, y: x ^ y, bits[:i + 1], 0) for i in range(len(bits))]
