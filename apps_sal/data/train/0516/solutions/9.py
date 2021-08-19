t = int(input())
for jack in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    r1 = 0
    for i in range(n - 1):
        m = 0
        for j in range(i + 1, n):
            if a[i] > a[j]:
                m += 1
        r1 += m
    a.sort()
    (last, r2) = (0, 0)
    for i in range(n):
        if a[i] != a[i - 1]:
            r2 += i
            last = i
        else:
            r2 += last
    r = r1 * k + k * (k - 1) * r2 // 2
    print(r)
