def alternate_sort(l):
    xs = sorted(l)
    pos, neg, result = [], [], []
    for x in xs:
        [pos, neg][x < 0].append(x)
    while pos and neg:
        result.extend([neg.pop(), pos.pop(0)])
    return result + neg[::-1] + pos
