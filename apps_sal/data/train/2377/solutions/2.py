t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] * n + i
    a.sort()
    p = [0 for _ in range(n)]
    for i in range(n):
        p[a[i]%n] = i
    q = [0 for _ in range(n)]
    for i in range(n):
        q[p[i]] = i
    cnt = 1
    m = 0
    for i in range(1, n):
        if q[i-1] < q[i]:
            cnt += 1
        else:
            m = max(cnt, m)
            cnt = 1
    m = max(cnt, m)
    print(n - m)
