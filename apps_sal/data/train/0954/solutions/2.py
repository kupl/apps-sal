t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    for i in range(1, n + 1):
        ans += i * i * i
    m = n - 1
    while m >= 1:
        ans += m * m * m
        m -= 1
    print(ans)
