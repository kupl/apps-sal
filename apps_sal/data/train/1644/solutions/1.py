import struct
b91abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'


def b91decode(strng):
    (a, b, c) = (-1, 0, 0)
    result = bytearray()
    for char in strng:
        if not char in b91abc:
            continue
        ind = b91abc.index(char)
        if a < 0:
            a = ind
        else:
            a += ind * 91
            b |= a << c
            c += 13 if a & 8191 > 88 else 14
            while True:
                result += struct.pack('B', b & 255)
                b >>= 8
                c -= 8
                if c <= 7:
                    break
            a = -1
    if a + 1:
        result += struct.pack('B', (b | a << c) & 255)
    return result.decode()


def b91encode(strng):
    (a, b) = (0, 0)
    result = ''
    for count in range(len(strng)):
        byte = strng.encode()[count:count + 1]
        b |= struct.unpack('B', byte)[0] << a
        a += 8
        if a > 13:
            c = b & 8191
            if c > 88:
                b >>= 13
                a -= 13
            else:
                c = b & 16383
                b >>= 14
                a -= 14
            result += b91abc[c % 91] + b91abc[c // 91]
    if a:
        result += b91abc[b % 91]
        if a > 7 or b > 90:
            result += b91abc[b // 91]
    return result
