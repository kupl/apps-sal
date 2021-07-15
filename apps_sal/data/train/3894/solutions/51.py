def solve(s):
    up = 0
    for c in s:
        if c.isupper():
            up += 1
    if up > len(s)/2:
        return s.upper()
    else:
        return s.lower()
