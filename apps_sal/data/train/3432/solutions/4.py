def shift(s=1):
    yield 0
    while 1:
        yield s
        s += 1
        yield s
        yield (s - 2)


def cipher(s):
    return ''.join((c if c == ' ' else chr((x + ord(c) - 97) % 26 + 97) for (c, x) in zip(s, shift())))
