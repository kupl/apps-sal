def solve(s):
    return sum(i for i, x in enumerate(s, 1) if x in '13579')
