def bin2gray(bits):
    g = [bits[0]] * len(bits)
    for i in range(1, len(bits)):
        g[i] = bits[i] ^ bits[i - 1]
    return g


def gray2bin(bits):
    b = [bits[0]] * len(bits)
    for i in range(1, len(bits)):
        b[i] = bits[i] ^ b[i - 1]
    return b

