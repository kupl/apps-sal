for _ in range(int(input())):
    s = input()
    n = len(s)
    t = 0
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            t = t + 1
    x = t
    for i in range(n):
        t = x
        if i != 0:
            if s[i] == s[i - 1]:
                t = t - 1
            else:
                t = t + 1
        y = t
        for j in range(i, n):
            t = y
            try:
                if s[j] == s[j + 1]:
                    t = t - 1
                else:
                    t = t + 1
            except:
                pass
            ans = ans + t
    print(ans)
