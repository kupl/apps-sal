def bin2gray(bits):
    return [x ^ y for (x, y) in zip(bits, [0] + bits)]


def gray2bin(bits):
    return [reduce(lambda x, y: x ^ y, bits[:i + 1]) for (i, _) in enumerate(bits)]
