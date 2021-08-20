rings = dict(dict.fromkeys('B', 2), **dict.fromkeys('ADOPRQaobdpqeg', 1))


def olympic_ring(s):
    score = sum((rings.get(c, 0) for c in s)) // 2
    return 'Not even a medal!' if score <= 1 else 'Bronze!' if score == 2 else 'Silver!' if score == 3 else 'Gold!'
