def solve(s):
    r = list(s.replace(' ', ''))
    return ''.join(i if i == ' ' else r.pop() for i in s)
