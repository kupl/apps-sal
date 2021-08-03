from fractions import Fraction


def on_line(ps):
    ps = list(set(ps))
    if ps and all(isinstance(x, int) for x in ps):
        return True
    return len({
        (x1 if x1 == x2 else Fraction(y2 - y1, x2 - x1))
        for (x1, y1), (x2, y2) in zip(ps, ps[1:])
    }) <= 1
