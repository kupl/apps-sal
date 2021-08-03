from collections import Counter

PTS_SUB_FUNCS = [lambda c: (1000, c, len(c) == 6),
                 lambda c: (750, c, set(c.values()) == {2} and len(c) == 3),
                 lambda c: next((((100 * n + 900 * (n == 1)) * (c[n] - 2), Counter([n] * c[n]), True) for n in range(1, 7) if c[n] >= 3), (0, 0, False)),
                 lambda c: (100 * c[1] + 50 * c[5], Counter([1] * c[1] + [5] * c[5]), bool(set(c.keys()) & {1, 5}))]


def get_score(dice):
    s, c = 0, Counter(dice)
    for f in PTS_SUB_FUNCS:
        while True:
            pts, subtractC, isThere = f(c)
            if isThere:
                c, s = c - subtractC, s + pts
            else:
                break
    return s or "Zonk"
