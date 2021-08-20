def solve(s):
    it = iter(s.replace(' ', '')[::-1])
    return ''.join((' ' if c == ' ' else next(it) for c in s))
