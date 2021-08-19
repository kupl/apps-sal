def solve(s):
    ys = iter((y for y in reversed(s) if y != ' '))
    return ''.join((next(ys) if x != ' ' else x for x in s))
