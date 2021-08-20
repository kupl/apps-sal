def solve(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper() == True:
            upper += 1
        else:
            lower += 1
    if upper > lower:
        s = s.upper()
    else:
        s = s.lower()
    return s
