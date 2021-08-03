def to_utf8_binary(string):
    return ''.join(format(c, '08b') for c in string.encode())


def from_utf8_binary(bitstring):
    bytes_ = [bitstring[i:i + 8] for i in range(0, len(bitstring), 8)]
    return bytes(int(byte, 2) for byte in bytes_).decode()
