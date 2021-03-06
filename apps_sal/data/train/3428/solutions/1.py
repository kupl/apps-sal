def scanner(qrcode):
    (Y, X) = (len(qrcode) - 1, len(qrcode[0]) - 1)
    (x, y, dir) = (X, Y, -1)
    bits = ''
    while len(bits) < 76:
        for i in range(2):
            bits += str(qrcode[x][y - i] ^ ((x + y - i) % 2 == 0))
        x += dir
        if x == 8 or x > X:
            dir = dir * -1
            x += dir
            y -= 2
    size = int(bits[4:12], 2)
    return ''.join((chr(int(bits[i:i + 8], 2)) for i in range(12, size * 8 + 12, 8)))
