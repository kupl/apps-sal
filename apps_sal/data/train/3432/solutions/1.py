from itertools import count

BASE = ord('a')


def deltas():
    for i in count(-1):
        yield max(i, 0)
        yield i + 2
        yield i + 3


def cipher(phrase):
    return ''.join(
        c if c.isspace() else chr(BASE + (ord(c) - BASE + delta) % 26)
        for c, delta in zip(phrase, deltas())
    )
