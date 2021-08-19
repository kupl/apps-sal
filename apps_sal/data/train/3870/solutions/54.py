def solve(s):
    (rev, s) = (s[::-1].replace(' ', ''), list(s))
    for i in range(len(s)):
        if s[i] != ' ':
            (s[i], rev) = (rev[0], rev[1:])
    return ''.join(s)
