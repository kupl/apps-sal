def scanner(qrc):
    bits = ''.join(str(qrc[x][y] ^ ((x + y) % 2 == 0)) for x, y in ticTocGen())
    size = int(bits[4:12], 2)
    return ''.join(chr(int(bits[i:i + 8], 2)) for i in range(12, 12 + 8 * size, 8))


def ticTocGen():
    x, y, dx = 20, 20, -1
    while y > 13:
        yield from ((x, y - dy) for dy in range(2))
        x += dx
        if x == 8 or x > 20:
            dx *= -1
            y -= 2
            x = x == 8 and 9 or 20
