t = int(input())
while(t):
    t -= 1
    n = int(input())
    x = []
    h = []
    for i in range(n):
        xi, hi = [int(i) for i in input().split()]
        x.append(xi)
        h.append(hi)
    diff = [x[1] - x[0], x[n - 1] - x[n - 2]]
    for i in range(1, n - 1):
        diff.append(x[i + 1] - x[i - 1])
    diff.sort()
    h.sort()
    ans = 0
    for i in range(n):
        ans += h[i] * diff[i]
    print(ans)
