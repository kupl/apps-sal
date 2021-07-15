def solve(s):
    return sum(i for i, c in enumerate(s, 1) if c in "13579")
