def solve(s):

    up, lw = 0, 0

    for i in s:
        if i.isupper():
            up += 1
        else:
            lw += 1

    if lw >= up:
        return s.lower()

    else:
        return s.upper()
