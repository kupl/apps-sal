def solve(s):
    s_rev = s[::-1].replace(' ', '')
    for i in range(len(s)):
        if s[i] == ' ':
            s_rev = s_rev[:i] + ' ' + s_rev[i:]
    return s_rev
