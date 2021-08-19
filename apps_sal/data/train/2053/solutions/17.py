(n, m) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dop = sum(a) * m
a.sort()
b.sort()
if a[-1] > b[0]:
    print(-1)
else:
    ans = 0
    for i in range(m):
        ans += b[i]
    if a[-1] == b[0]:
        ans -= a[-1] * m
    else:
        ans -= a[-1] * (m - 1)
        ans -= a[-2]
    ans = ans + dop
    print(ans)
