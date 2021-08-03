def bin_to_hex(binary_string):

    n = sum(2**i for i, b in enumerate(binary_string[::-1]) if b == '1')

    return '{:x}'.format(n)


def hex_to_bin(hex_string):

    def convert(x): return ord(x) - 48 if 48 <= ord(x) <= 57 else ord(x.lower()) - 87

    n = sum(convert(x) * 16**i for i, x in enumerate(hex_string[::-1]))

    return '{:b}'.format(n)
