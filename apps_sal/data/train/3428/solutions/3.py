def coords():
    rs = range(9, 21)
    for c in [20, 16]:
        for i in reversed(rs):
            yield i, c
            yield i, c - 1
        for i in rs:
            yield i, c - 2
            yield i, c - 3


def scanner(qrcode):
    it = (qrcode[r][c] ^ (1 - (r + c) % 2) for r, c in coords())
    bstring = "".join(map(str, it))
    offset = 12
    length = int(bstring[4:offset], 2)
    bstring = bstring[offset: offset + length * 8]
    return "".join(chr(int("".join(xs), 2)) for xs in zip(*[iter(bstring)] * 8))
