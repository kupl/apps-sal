def solve(s):
    return sum(i + 1 for i, d in enumerate(list(s)) if d in '13579')
