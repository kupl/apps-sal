def solve(s):
    rs = s[::-1].replace(' ', '')
    for i in range(len(s)):
        if s[i] == ' ':
            rs = rs[:i] + ' ' + rs[i:]
    return rs
