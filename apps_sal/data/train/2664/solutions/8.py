def solve(s):
    dif = sum((a != b for (a, b) in zip(s, s[::-1])))
    return dif == 2 or (not dif and len(s) & 1)
