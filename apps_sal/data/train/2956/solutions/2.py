def encode(string):
    return ''.join(map('{:08b}'.format, string.encode())).replace('0', '000').replace('1', '111')


def decode(bits):
    bytes_ = ('01'['11' in a + b + c + a] for (a, b, c) in zip(*[iter(bits)] * 3))
    return bytes((int(''.join(b), 2) for b in zip(*[iter(bytes_)] * 8))).decode()
