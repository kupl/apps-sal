def get(c1, c2):
    if c1 > c2:
        t = c1
        c1 = c2
        c2 = t
    if c1 == c2:
        return c1
    if c1 == 'B':
        if c2 == 'G':
            return 'R'
        else:  # c2 R
            return 'G'
    if c1 == 'G':
        if c2 == 'R':
            return 'B'
    return 1 + 'a'


def triangle(x):
    if len(x) == 1:
        return x
    else:
        xx = [get(x[i], x[i + 1]) for i in range(len(x) - 1)]
        return triangle(''.join(xx))
