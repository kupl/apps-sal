t = int(input())
for test in range(t):
    n, m = map(int, input().split())
    length = 1
    a = [0] * 10
    cur = m % 10
    a[cur] = 1
    s = cur
    while True:
        cur += m
        cur %= 10
        if a[cur] == 1:
            break
        else:
            length += 1
            s += cur
            a[cur] = 1
    ost = 0
    cur = n // (m * length) * (m * length)
    while cur <= n:
        ost += cur % 10
        cur += m
    print(n // (m * length) * s + ost)
