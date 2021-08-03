def solve(s):
    if len(s) < 2:
        return s
    if s[0] == ' ':
        return ' ' + solve(s[1:])
    if s[-1] == ' ':
        return solve(s[:-1]) + ' '
    return s[-1] + solve(s[1:-1]) + s[0]
