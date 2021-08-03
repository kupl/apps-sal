for _ in range(int(input())):
    s = list(input())
    n = len(s)
    an = 1
    mod = 10000009
    for i in range(n):
        if s[i] == "?" and s[n - i - 1] == "?":
            an = (an * 26) % mod
            s[i] = "."
            s[n - i - 1] = "."
        elif s[i] != "?" and s[n - i - 1] != "?":
            if s[i] != s[n - i - 1]:
                an = 0
                break
    print(an % mod)
