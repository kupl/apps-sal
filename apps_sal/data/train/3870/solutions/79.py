def solve(s):
    r = s.replace(' ','')[::-1]
    for i in range(len(s)):
        if s[i] == ' ': r = r[:i] + ' ' + r[i:]
    return r
