def solve(s):
    return 'OK' if s == s[::-1] else 'remove one' if any(s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] for i in range(len(s))) else 'not possible'
