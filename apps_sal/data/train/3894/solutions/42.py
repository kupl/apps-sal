
def solve(s):
    lower = 0
    for x in s:
        if x.islower():
            lower += 1
    upper = 0
    for x in s:
        if x.isupper():
            upper += 1
    if lower >= upper:
        return s.lower()
    else:
        return s.upper()
