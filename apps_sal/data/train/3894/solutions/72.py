def solve(s):
    countU = 0
    countL = 0
    for x in s:
        if x.isupper():
            countU += 1
        else:
            countL += 1
    if countU > countL:
        return s.upper()
    else:
        return s.lower()
