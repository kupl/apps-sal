def solve(s):
    if s == s[::-1]:
        return 'OK'
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return 'remove one'
    return 'not possible'
