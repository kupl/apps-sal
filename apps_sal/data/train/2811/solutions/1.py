from itertools import groupby


def send(s):
    return toUnary(''.join((f'{ord(c):0>7b}' for c in s)))


def toUnary(c):
    return ' '.join((f"{'0' * (2 - int(b))} {'0' * sum((1 for _ in g))}" for (b, g) in groupby(c)))


def receive(s):
    it = iter(s.split())
    binS = ''.join((str(len(b) & 1) * len(n) for (b, n) in zip(it, it)))
    return ''.join((chr(int(binS[i:i + 7], 2)) for i in range(0, len(binS), 7)))
