def solve(s):
    r = [a for a in s if a != ' ']
    return ''.join((a if a == ' ' else r.pop() for a in s))
