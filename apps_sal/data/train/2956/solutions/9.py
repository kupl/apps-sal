def encode(string):
    ascii_bits = []
    for char in string:
        ascii_bits.append(f'{ord(char):08b}'.replace('0', '000').replace('1', '111'))

    return "".join(ascii_bits)


def decode(bits):
    chunked_bits = []
    for i in range(0, len(bits), 3):
        chunked_bits.append(bits[i:i + 3])
    dechunked_bits = []

    for bit in chunked_bits:
        if bit.count('1') >= 2:
            dechunked_bits.append('1')
        else:
            dechunked_bits.append('0')

    dechunked_bits = "".join(dechunked_bits)
    converted_ascii = []

    for j in range(0, len(dechunked_bits), 8):
        converted_ascii.append(chr(int(dechunked_bits[j:j + 8], 2)))

    converted_ascii = "".join(converted_ascii)
    print(converted_ascii)

    return converted_ascii
