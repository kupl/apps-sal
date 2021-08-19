codes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'


def b91decode(strng):
    b = []
    for i in range(0, len(strng), 2):
        if len(strng[i:i + 2]) == 2:
            (c1, c2) = strng[i:i + 2]
            x = codes.index(c1) + codes.index(c2) * 91
        else:
            x = codes.index(strng[i:i + 2])
        if x <= 88 or x >= 8192:
            b = list('{:014b}'.format(x)) + b
        else:
            b = list('{:013b}'.format(x)) + b
    r = ''
    while b:
        x = []
        for _ in range(8):
            if not b:
                break
            x.insert(0, b.pop())
        r += chr(int(''.join(x), 2))
    return r.rstrip('\x00')


def b91encode(strng):
    b = []
    for c in strng:
        b = list('{:08b}'.format(ord(c))) + b
    r = ''
    while b:
        x = []
        for _ in range(13):
            if not b:
                break
            x.insert(0, b.pop())
        n = int(''.join(x), 2)
        if n <= 88 and b:
            x.insert(0, b.pop())
            n = int(''.join(x), 2)
        r += codes[n % 91] + codes[n // 91]
    return r.rstrip('A')
