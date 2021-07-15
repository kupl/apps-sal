def bin(mas,x):
    l = 0
    r = len(mas)
    while (r > l + 1):
        m = (r + l) // 2;
        if (x < mas[m]):
            r = m;
        else:
            l = m
    return l

n = int(input())
a = [-9999999]
b = [9999999]
dp = [0] * (n + 1)
for i in range(n):
    x,y=[int(i) for i in input().split()]
    a.append(x)
    b.append(y)

a, b = (list(x) for x in zip(*sorted(zip(a, b))))



for i in range(1,n+1):
    z = a[i] - b[i] - 1
    x = bin(a, z)
    dp[i] = dp[x] + ( i - x - 1)
ans = 10**30
for i in range(1, n + 1):
    ans = min(ans, dp[i] + n - i)
print(ans)
