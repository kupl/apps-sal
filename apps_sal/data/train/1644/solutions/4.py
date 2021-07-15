# yet another rewrite of Joachim Henke's C# implementation

ENCODE = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\"")
DECODE = dict(map(reversed, enumerate(ENCODE)))

def b91encode(s):
    b, i = 0, 0
    r = ""

    for c in s:
        b |= ord(c) << i
        i += 8
        if i > 13:
            v = b & 0x1FFF
            k = 13
            if v < 89:
                v = b & 0x3FFF
                k += 1
            b >>= k
            i -= k
            r += ENCODE[v % 91] + ENCODE[v // 91]
    if i:
        r += ENCODE[b % 91]
        if i > 7 or b > 90: r += ENCODE[b // 91]

    return r

def b91decode(s):
    v, b, i = -1, 0, 0
    r = ""

    for c in s:
        c = DECODE[c]
        if ~v:
            v += c * 91
            b |= v << i
            i += 13 + (v & 0x1FFF < 89)
            while 1:
                r += chr(b & 0xFF)
                b >>= 8
                i -= 8
                if i < 8: break
            v = -1
        else: v = c
    if ~v: r += chr((b | v << i) & 0xFF)

    return r
