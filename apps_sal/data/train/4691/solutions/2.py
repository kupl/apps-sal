def solve(s):
    res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res
