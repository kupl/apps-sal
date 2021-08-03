from collections import Counter

COUNTS = [
    (50, lambda s, _: len(set(s)) == 1),
    (40, lambda _, c: len(c) == 2 and 4 in c.values()),
    (30, lambda _, c: set(c.values()) == {2, 3}),
    (20, lambda s, _: (s := ''.join(sorted(s))) in '123456' or s == '13456'),
]


def points(dice):
    c = Counter(dice)
    return sum(pts for pts, isValid in COUNTS if isValid(dice, c))
