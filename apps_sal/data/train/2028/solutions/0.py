def solve(s):
    n = len(s)
    for i in range(n):
        s2 = s[i:] + s[:i]
        if s != s2 and s2[::-1] == s2:
            return 1
    for i in range(n // 2 + 1, n):
        if s[i] != s[0]:
            return 2
    return 'Impossible'


s = input()
print(solve(s))
