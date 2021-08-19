for _ in range(int(input())):
    ans = 0
    (n, m) = list(map(int, input().split()))
    a = []
    if m > n:
        print('0')
        continue
    for i in range(10):
        a.append(m * (i + 1) % 10)
    s = sum(a)
    ans += n // (m * 10) * s
    k = n % (10 * m)
    p = k // m
    for i in range(p):
        ans += a[i]
    print(ans)
