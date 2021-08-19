def solve(s):
    (u, l) = (0, 0)
    for i in s:
        if i.isupper():
            u += 1
        else:
            l += 1
    return s.lower() if l >= u else s.upper()
