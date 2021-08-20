def to_utf8_binary(string):
    return ''.join((bin(i)[2:].zfill(8) for i in string.encode('utf-8')))


def from_utf8_binary(bitstr):
    byte_str = bytes((int(bitstr[i:i + 8], 2) for i in range(0, len(bitstr), 8)))
    return byte_str.decode('utf-8')
