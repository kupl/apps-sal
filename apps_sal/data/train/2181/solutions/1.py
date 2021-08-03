n = int(input())
a = list(map(int, input().strip().split()))
if n > 1:
    li = [0] * n
    ri = [0] * n
    lm = a[0]
    c = [0] * n
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        if lm >= a[i]:
            li[i] = li[i - 1] + (lm + 1 - a[i])
            lm = lm + 1
        else:
            li[i] = li[i - 1]
            lm = a[i]
        b[i] = lm
    lm = a[n - 1]
    c[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        if lm >= a[i]:
            ri[i] = ri[i + 1] + (lm + 1 - a[i])
            lm = lm + 1
        else:
            ri[i] = ri[i + 1]
            lm = a[i]
        c[i] = lm
    ans = 1 << 64
    for i in range(n):
        if i == 0:
            ans = min(ans, ri[i], ri[i + 1])
        elif i == n - 1:
            ans = min(ans, li[i], li[i - 1])
        else:
            v1 = li[i] + ri[i + 1]
            if b[i] == c[i + 1]:
                v1 += 1
            v2 = ri[i] + li[i - 1]
            if c[i] == b[i - 1]:
                v2 += 1
            val = min(v1, v2)
            ans = min(ans, val)
    print(ans)
else:
    print(0)
