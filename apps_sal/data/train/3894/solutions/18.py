def solve(s):
    uppercount = 0
    for i in s:
        if i.isupper():
            uppercount += 1
        if uppercount > len(s)/2:
            s = s.upper()
        else:
            s = s.lower()
    return s
