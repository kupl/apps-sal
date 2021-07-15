def solve(s):
    return sum(i for i, n in enumerate(s, 1) if int(n) % 2)
