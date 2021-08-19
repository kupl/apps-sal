# cook your dish here
for _ in range(int(input())):
    l, n, x = map(int, input().split())
    m = []
    pw1 = (1 << 17)
    pw2 = (1 << 18)
    if (n == 1):
        m.append(x)
    elif (n == 2 and x == 0):
        m.append(-1)
    elif (n == 2):
        m.append(x)
        m.append(0)
    else:
        ans = 0
        for i in range(1, n - 2):
            m.append(i)
            ans = ans ^ i
        if (ans == x):
            m.append(pw1 + pw2)
            m.append(pw1)
            m.append(pw2)
        else:
            m.append(pw1)
            m.append((pw1 ^ x) ^ ans)
            m.append(0)
    p = (m) * l
    for i in range(0, l):
        print(p[i], end=' ')
    print()
