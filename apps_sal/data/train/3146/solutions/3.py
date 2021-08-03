def to_utf8_binary(s):
    return ''.join("{:08b}".format(x) for x in bytearray(s, 'utf-8'))


def from_utf8_binary(s):
    bs = []
    for i in range(0, len(s), 8):
        bs.append(int(s[i:i + 8], 2))
    return bytearray(bs).decode('utf-8')
