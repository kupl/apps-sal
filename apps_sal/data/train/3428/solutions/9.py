def up(x0, y0):
    return tuple((x, y) for y in range(y0+3, y0-1, -1) for x in (x0+1, x0))
def down(x0, y0):
    return tuple((x, y) for y in range(y0, y0+4) for x in (x0+1, x0))
def top(x0, y0):
    return ((x0+3, y0+1), (x0+2, y0+1)) + tuple((x, y0) for x in range(x0+3, x0-1, -1)) + ((x0+1, y0+1), (x0, y0+1))
def bot(x0, y0):
    return ((x0+3, y0), (x0+2, y0)) + tuple((x, y0+1) for x in range(x0+3, x0-1, -1)) + ((x0+1, y0), (x0, y0))

modebits = (20,20), (19,20), (20,19), (19,19)
lenbits = up(19,15)
bits = (
    up(19,11), top(17,9), down(17,11), down(17,15), bot(15,19), up(15,15), up(15,11), top(13,9),
    down(13,11), down(13,15), bot(11,19), up(11,15), up(11,11), up (11,7), up(11,2), top(9,0), down(9,2))

def num(code, bits):
    n = 0
    for x, y in bits:
        n = (n << 1) + (code[y][x] ^ (x+y)%2 ^ 1)
    return n

def scanner(qrcode):
    mode = num(qrcode, modebits)
    length = num(qrcode, lenbits)
    print(f'{mode=}, {length=}')
    return ''.join(chr(num(qrcode, bits[i])) for i in range(length))
