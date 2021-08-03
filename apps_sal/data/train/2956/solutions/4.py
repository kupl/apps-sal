def encode(string):
    bits = ""
    for i in string:
        bits += '{0:08b}'.format(ord(i))

    return bits.replace('1', '111').replace('0', '000')


def decode(bits):
    x = 3
    res = [bits[y - x:y] for y in range(x, len(bits) + x, x)]

    decoded = ""
    for i in res:
        sorti = sorted(i)
        decoded += sorti[1]

    x = 8
    bin = [decoded[y - x:y] for y in range(x, len(decoded) + x, x)]

    return "".join([chr(int(x, 2)) for x in bin])
