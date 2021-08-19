def solve(s):
    new_s = reversed(s.replace(' ', ''))
    return ''.join((i if i == ' ' else next(new_s) for i in s))
