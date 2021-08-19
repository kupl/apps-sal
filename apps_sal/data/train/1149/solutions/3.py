for _ in range(int(input())):
    s = list(input())
    n = len(s)
    (S, mod) = (1, 10000009)
    for i in range(n):
        if s[i] == '?' and s[n - i - 1] == '?':
            S = S * 26 % mod
            (s[i], s[n - i - 1]) = ('.', '.')
        elif s[i] != '?' and s[n - i - 1] != '?':
            if s[i] != s[n - i - 1]:
                S = 0
                break
    print(S % mod)
