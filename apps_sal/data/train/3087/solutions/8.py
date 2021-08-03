def solve(s):
    if s == s[::-1]:
        return "OK"
    for i in range(len(s)):
        news = s[:i] + s[i + 1:]
        if news == news[::-1]:
            return "remove one"
    return "not possible"
