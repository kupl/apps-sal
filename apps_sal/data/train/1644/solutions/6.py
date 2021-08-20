from struct import pack, unpack
base91 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
decode_table = {v: k for (k, v) in enumerate(base91)}


def b91encode(string):
    b = n = 0
    out = ''
    for i in range(len(string)):
        byte = string.encode('utf-8')[i:i + 1]
        b |= unpack('B', byte)[0] << n
        n += 8
        if n > 13:
            v = b & 8191
            if v > 88:
                b >>= 13
                n -= 13
            else:
                v = b & 16383
                b >>= 14
                n -= 14
            out += base91[v % 91] + base91[v // 91]
    if n:
        out += base91[b % 91]
        if n > 7 or b > 90:
            out += base91[b // 91]
    return out


def b91decode(string):
    v = -1
    b = n = 0
    out = bytearray()
    for char in string:
        if char not in decode_table:
            continue
        c = decode_table[char]
        if v < 0:
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if v & 8191 > 88 else 14
            while True:
                out += pack('B', b & 255)
                b >>= 8
                n -= 8
                if not n > 7:
                    break
            v = -1
    if v + 1:
        out += pack('B', (b | v << n) & 255)
    return out.decode('utf-8')
