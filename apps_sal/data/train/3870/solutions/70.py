def solve(s):
    m = s.replace(' ','')
    r = ''
    i = -1
    for c in s:
        if c!=' ':
            r += m[i]
            i -= 1
        else:
            r += ' '
    return r
