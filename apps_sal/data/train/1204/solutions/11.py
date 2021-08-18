t = int(input())
while (t != 0):
    s = input()
    r = input()
    n = len(s)
    k = 0
    c = 0
    crlen = 0
    ans = 0
    j = 0
    a = []
    for i in range(0, n, 1):
        if (s[i] != r[i]):
            if(crlen > 0 and j == 1):
                a.append(crlen)
                k = k + 1
            elif (j == 0):
                k = k + 1
            crlen = 0
            j = 1
            c = c + 1

        else:
            crlen = crlen + 1
    a.sort()
    ans = c * k
    for i in a:
        c = c + i
        k = k - 1
        ans = min(ans, c * k)
    print(ans)
    t = t - 1
