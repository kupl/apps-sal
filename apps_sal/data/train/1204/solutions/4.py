for _ in range(int(input())):
    s = list(input())
    r = list(input())
    l = []
    flag = 0
    eq = 0
    k = 0
    s_1 = 0
    for i in range(len(s)):
        if s[i] != r[i]:
            if eq > 0 and flag == 1:
                l.append(eq)
                k += 1
            elif flag == 0:
                k += 1
            eq = 0
            flag = 1
            s_1 += 1
        else:
            eq += 1
    l.sort()
    res = 0
    res = k * s_1
    for i in range(len(l)):
        s_1 = s_1 + l[i]
        k = k - 1
        res = min(res, s_1 * k)
    print(res)
