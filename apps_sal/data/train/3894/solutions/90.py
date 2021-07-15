def solve(s):
    u = 0
    l = 0
    for x in s:
        if x.isupper():
            u+=1
        else:
            l+=1
    if l>=u:
        return s.lower()
    return s.upper()
