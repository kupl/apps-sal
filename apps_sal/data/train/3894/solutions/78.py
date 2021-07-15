def solve(s):
    res = 0
    for i in [x for x in s]:
        if i.isupper():
            res += 1
        else:
            res -= 1
    return s.lower() if res <= 0 else s.upper() 
