for i in range(int(input())):
    s = input()
    s1 = input()
    k, l, g = 0, 0, 0
    gp = []
    f = False
    for i in range(len(s)):
        if s[i] == s1[i]:
            if f:
                g += 1
        else:
            if not f:
                k += 1
            f = True
            l += 1
            if g > 0:
                k += 1
                gp.append(g)
                g = 0
    gp.sort()
    res = k * l
    for i in range(len(gp)):
        l += gp[i]
        k -= 1
        res = min(res, k * l)
    print(res)
