def solve(s):
    cup, clw = 0, 0
    for c in s:
        if c.isupper():
            cup += 1
            if cup > len(s) / 2:
                return s.upper()
        else:
            clw += 1
            if clw > len(s) / 2:
                return s.lower()
    else:
        return s.lower()
