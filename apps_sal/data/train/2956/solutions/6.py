def encode(string):
    ASCII = [ord(c) for c in string]
    BIN = [format(i, '08b') for i in ASCII]
    bits = ''.join([BIN[i].replace("1", "111").replace("0", "000") for i in range(0, len(BIN))])
    return bits


def decode(bits):
    a = [list(bits[i:i + 3]) for i in range(0, len(bits), 3)]
    b = [int(a[i][j]) for i in range(0, len(a)) for j in range(0, 3)]
    c = [list(b[i:i + 3]) for i in range(0, len(bits), 3)]
    d = []
    for i in range(0, len(bits) // 3):
        if sum(c[i]) >= 2:
            d.append('1')
        else:
            d.append('0')
    e = ''.join(d)
    n = int(e, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
