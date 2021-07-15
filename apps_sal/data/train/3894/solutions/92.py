def solve(s):
    l=0
    z=0
    for b in s:
        if b.islower():
            l+=1
        else:
            z+=1
    if l>=z:
        return s.lower()
    else:
        return s.upper()
