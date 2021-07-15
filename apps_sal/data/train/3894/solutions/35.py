def solve(s):
    upr = 0
    lwr = 0
    for i in s:
        if i.isupper():
            upr += 1
        else:
            lwr += 1
    if upr > lwr:
        return s.upper()
    else:
        return s.lower()
