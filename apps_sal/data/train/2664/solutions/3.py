def solve(s):
    h = len(s) // 2
    diffs = sum((1 for (a, b) in zip(s[:h], s[-h:][::-1]) if a != b))
    return diffs == 1 or (diffs == 0 and len(s) % 2 == 1)
