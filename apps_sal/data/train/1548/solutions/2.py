t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))[:n]
    for i in range(1, n):
        l[i] = min(l[i - 1] + 1, l[i])
    for j in range(n - 2, -1, -1):
        l[j] = min(l[j + 1] + 1, l[j])
    print(*l)
