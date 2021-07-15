def solve(s):
    l = 0
    u = 0
    for x in s:
        if x.islower():
            l += 1
        else:
            u += 1
    if l >= u:
        return s.lower()
    else:
        return s.upper()
