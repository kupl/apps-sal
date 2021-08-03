def decode(binary):
    *b, p = binary
    if '01'[b.count('1') % 2] != p:
        return 'error'
    return binary[:-1]


def parity_bit(binaries):
    return ' '.join(decode(binary) for binary in binaries.split())
