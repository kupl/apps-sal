def solve(s):
    z = reversed(s.replace(' ', ''))
    return ''.join(' ' if i == ' ' else next(z) for i in s)
