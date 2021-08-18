t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        a.append(x)
        b.append(y)
    b.sort()
    xcor = []
    xcor.append(a[1] - a[0])
    xcor.append(a[n - 1] - a[n - 2])
    for i in range(1, n - 1):
        xcor.append(a[i + 1] - a[i - 1])
    xcor.sort()
    ans = 0
    for i in range(n):
        ans = ans + xcor[i] * b[i]
    print(ans)
