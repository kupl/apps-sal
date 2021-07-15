def solve(s):
    n = len(s) // 2
    up = 0
    for i in s:
        if i.isupper():
            up += 1
    if up > n:
        return s.upper()
    return s.lower()
