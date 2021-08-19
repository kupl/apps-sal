t = int(input())
for i in range(t):
    (n, k, l) = list(map(int, input().split()))
    (m, v) = ([], [])
    for i in range(1, n + 1):
        v.append(i)
    if n > k * l or (k == 1 and n > 1):
        print(-1)
    else:
        for i in range(n):
            m.append(v[i % k])
        print(*m)
