def solve(s):
    l = 0
    u = 0

    for i in s:
        if i.islower():
            l += 1
        else:
            u += 1
    if l > u:
        return s.lower()
    elif u > l:
        return s.upper()
    elif u == l:
        return s.lower()
