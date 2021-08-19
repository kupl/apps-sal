def solve(a, b):
    c1 = 0
    c2 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            c1 += 1
        elif a[i] == b[i]:
            pass
        else:
            c2 += 1
    if c1 == c2:
        return '{}, {}: that looks like a "draw"! Rock on!'.format(c1, c2)
    elif c1 > c2:
        return '{}, {}: Alice made "Kurt" proud!'.format(c1, c2)
    else:
        return '{}, {}: Bob made "Jeff" proud!'.format(c1, c2)
