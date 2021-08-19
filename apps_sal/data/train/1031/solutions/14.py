from math import sqrt
t = int(input())
for qq in range(t):
    (h, s) = list(map(float, input().split()))
    h2 = h ** 2
    h4 = h ** 4
    s2 = s ** 2
    D = h4 - 16.0 * s2
    if D < 0:
        print(-1)
    else:
        D = sqrt(D)
        r1 = h2 + D
        r1 /= float(2.0)
        r2 = h2 - D
        r2 /= float(2.0)
        if r1 > 0.0:
            a = r1
        elif r2 > 0.0:
            a = r2
        else:
            print(-1)
            continue
        a = sqrt(a)
        b = 2.0 * s
        b /= a
        ans = [a, b, h]
        ans.sort()
        print('%.20f %.20f %.20f' % (ans[0], ans[1], ans[2]))
