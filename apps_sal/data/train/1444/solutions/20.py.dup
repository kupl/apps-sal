for _ in range(int(input())):
    n = int(input())
    p = [int(o) for o in input().split()]
    s = [0] * n
    pr = [0] * n
    s[n - 1] = 1
    pr[n - 1] = 0
    if n - 2 >= 0:
        s[n - 2] = 2
        pr[n - 2] = 1
    if n - 3 >= 0:
        s[n - 3] = 3
        pr[n - 3] = 1
        if p[n - 3] == 2:
            s[n - 3] += 2
            pr[n - 3] += 1
    i = n - 4
    while i >= 0:
        s[i] = 1
        s[i] += s[i + 1]
        pr[i] = 1
        if p[i] == 2:
            s[i] += s[i + 2]
            s[i] += 1
            pr[i] += 1
            if p[i + 3] == 2:
                s[i] += pr[i + 2]
                pr[i] += pr[i + 2]
            if p[i + 1] == 2:
                s[i] += s[i + 3]
        s[i] = s[i] % 1000000007
        pr[i] = pr[i] % 1000000007
        i -= 1
    print(s[0])
