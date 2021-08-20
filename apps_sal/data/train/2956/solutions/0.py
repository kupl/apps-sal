def encode(stg):
    return ''.join((digit * 3 for char in stg for digit in f'{ord(char):08b}'))


def decode(binary):
    reduced = (get_digit(triplet) for triplet in chunks(binary, 3))
    return ''.join((get_char(byte) for byte in chunks(''.join(reduced), 8)))


def chunks(seq, size):
    return (seq[i:i + size] for i in range(0, len(seq), size))


def get_digit(triplet):
    return max(triplet, key=triplet.count)


def get_char(byte):
    return chr(int(byte, 2))
