t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    l = []
    for i in range(a):
        l.append(list(map(int, input().split())))
    k = []
    for i in range(b):
        x = 0
        y = 0
        (n, m) = (0, i)
        while n < a and m >= 0:
            if l[n][m] == 0:
                x += 1
            else:
                y += 1
            n += 1
            m -= 1
        k.append([x, y])
    for i in range(1, a):
        x = 0
        y = 0
        (n, m) = (i, b - 1)
        while n < a and m >= 0:
            if l[n][m] == 0:
                x += 1
            else:
                y += 1
            n += 1
            m -= 1
        k.append([x, y])
    ans = 0
    s = input()
    (p, q) = list(map(int, input().split()))
    for i in range(a + b - 1):
        if s[i] == '0':
            ans += min(k[i][1] * p, q + k[i][0] * p)
        else:
            ans += min(k[i][0] * p, q + k[i][1] * p)
    print(ans)
