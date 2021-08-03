def solve(s):
    rev_s = [*s.replace(' ', '')]
    return ''.join([rev_s.pop() if c != ' ' else ' ' for c in s])
