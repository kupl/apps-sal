def solve(s):
    ups = 0
    lows = 0
    for i in s:
        if i == i.upper():
            ups += 1
        else:
            lows += 1
    if ups == lows or lows > ups:
        return s.lower()
    return s.upper()
