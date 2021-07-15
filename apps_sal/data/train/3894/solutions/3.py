def solve(s):
    n = len(s) // 2
    upper_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        if upper_count > n:
            return s.upper()
    return s.lower()
