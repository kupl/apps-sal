def prod2sum(a, b, c, d):
    l1 = sorted([abs(a * c + b * d), abs(a * d - b * c)])
    l2 = sorted([abs(a * c - b * d), abs(a * d + b * c)])
    if l1 == l2:
        return [l1]
    else:
        return sorted([l1, l2])
