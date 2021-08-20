def solve(s):
    r = sum((a != b for (a, b) in zip(s, s[::-1])))
    return r == 2 or (r == 0 and len(s) % 2)
