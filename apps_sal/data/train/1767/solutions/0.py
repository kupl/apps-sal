from collections import Counter


def solution(tiles):
    return "".join(
        tile for tile in "123456789"
        if tiles.count(tile) < 4
        and list(meld(meld(meld(meld(pair(Counter(map(int, tiles + tile))))))))
    )


def pair(c):
    yield from (c - Counter([t, t]) for t in c if c[t] > 1)


def meld(C):
    yield from (
        c - m for c in C for t in [min(c.keys())]
        for m in (Counter((t, t + d, t + d + d)) for d in (0, 1))
        if (c & m) == m)
