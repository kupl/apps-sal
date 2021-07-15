def solve(s):
    r = [0] * 4
    for e in s:
        r[0 if e.isupper() else 1 if e.islower() else 2 if e.isdigit() else 3] += 1
    return r
