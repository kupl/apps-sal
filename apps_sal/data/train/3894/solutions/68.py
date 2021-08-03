def solve(s):
    list_1 = [char for char in s]
    x = 0
    for c in [char for char in s]:
        if c.isupper():
            x = x + 1
    if x > len(s) / 2:
        s = s.upper()
    else:
        s = s.lower()
    return s
