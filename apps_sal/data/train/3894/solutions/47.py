def solve(s):
    lowercount = 0
    uppercount = 0
    for x in s:
        for y in x:
            if y.islower():
                lowercount = lowercount + 1
            if y.isupper():
                uppercount = uppercount + 1
            print(y)
    if lowercount >= uppercount:
        s = s.lower()
    if lowercount < uppercount:
        s = s.upper()
    return s
