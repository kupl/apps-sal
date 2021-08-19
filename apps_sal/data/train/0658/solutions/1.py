# cook your dish here
t = int(input())
for j in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    up = [1] * (n + 1)
    dn = [1] * (n + 1)
    up[-1], dn[-1] = 0, 0
    for i in reversed(range(n - 1)):
        if x[i] <= x[i + 1]:
            dn[i] += up[i + 1]
        if x[i] >= x[i + 1]:
            up[i] += dn[i + 1]
    ans = 0
    for i in range(n):
        t = dn[i]
        if t % 2:
            t += dn[i + t]
        else:
            t += up[i + t]
        ans = max(ans, t + 1)
    print(ans)
