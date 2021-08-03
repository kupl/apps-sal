def bin2gray(bits):
    gray = []
    gray.append(bits[0])
    for index in range(1, len(bits), 1):
        gray.append(bits[index - 1] ^ bits[index])
    return gray


def gray2bin(bits):
    bin = []
    bin.append(bits[0])
    for index in range(1, len(bits), 1):
        bin.append(bin[index - 1] ^ bits[index])
    return bin
