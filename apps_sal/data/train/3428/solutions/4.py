from itertools import islice


def get_byte(it):
    return int(''.join(islice(it, 8)), 2)


def scanner(qrcode):

    def next_bit():
        (i, j) = (18, 20)
        while True:
            yield str(i & 1 ^ j & 1 ^ qrcode[i][j] ^ 1)
            if j % 2 == 0 or (i == 9 and j % 4 == 3) or (i == 20 and j % 4 == 1):
                j -= 1
            else:
                i += 1 if j % 4 == 1 else -1
                j += 1
    bits = next_bit()
    return ''.join((chr(get_byte(bits)) for _ in range(get_byte(bits))))
