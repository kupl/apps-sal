def packets(it, n):
    for i in range(0, len(it), n):
        yield it[i:i + n]


def encode(string):
    return ''.join(x * 3 for c in string for x in f"{ord(c):08b}")


def decode(bits):
    tmp = ''.join(s[0] if s[0] in s[1:] else s[1] for s in packets(bits, 3))
    return ''.join(chr(int(x, 2)) for x in packets(tmp, 8))
