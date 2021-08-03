def solve(s):
    c = 0
    for x in s:
        if x.isupper():
            c = c + 1
    if c > len(s) / 2:
        return s.upper()
    return s.lower()
