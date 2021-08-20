int = 0 .__class__
str = 'a'.__class__
CONVERSION = dict(enumerate('0123456789abcdef'))


def bin_to_hex(b):
    b = int(b, 2)
    result = []
    while True:
        (b, m) = divmod(b, 16)
        result.append(CONVERSION[m])
        if b == 0:
            break
    return ''.join(map(str, reversed(result)))


def hex_to_bin(b):
    b = int(b, 16)
    result = []
    while True:
        (b, m) = divmod(b, 2)
        result.append(m)
        if b == 0:
            break
    return ''.join(map(str, reversed(result)))
