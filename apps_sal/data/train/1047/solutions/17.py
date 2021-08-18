t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    d = []
    dl = []
    for i in range(n):
        x, y = map(int, input().split())
        d.append(y - x)
        dl.append(y + x)
    d = sorted(d)
    dl = sorted(dl)
    ans = abs(d[0] - d[1])
    k = 0
    while (k < n - 1):
        ans = min(ans, abs(d[k] - d[k + 1]))
        ans = min(ans, abs(dl[k] - dl[k + 1]))
        k += 1
    if (ans % 2 == 0):
        print(int(ans / 2))
    else:
        print(ans / 2)
