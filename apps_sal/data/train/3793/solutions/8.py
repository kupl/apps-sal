def triangle_type(a, b, c):
    if max(a, b, c) >= sum([a, b, c]) / 2:
        return 0
    sq = [max(a, b, c) ** 2, sum([x ** 2 for x in [a, b, c]]) / 2]
    return 3 if sq[0] > sq[1] else 2 if sq[0] == sq[1] else 1
