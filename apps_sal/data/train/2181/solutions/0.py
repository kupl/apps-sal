n = int(input())
a = list(map(int, input().split()))
(lp, rp) = ([0 for i in range(n)], [0 for i in range(n)])
(lnr, rnr) = ([a[i] for i in range(n)], [a[i] for i in range(n)])
mx = a[0]
for i in range(1, n):
    if a[i] > mx:
        mx = a[i]
        lp[i] = lp[i - 1]
    else:
        mx += 1
        lp[i] = lp[i - 1] + mx - a[i]
        lnr[i] = mx
mx = a[-1]
for i in range(n - 2, -1, -1):
    if a[i] > mx:
        mx = a[i]
        rp[i] = rp[i + 1]
    else:
        mx += 1
        rp[i] = rp[i + 1] + mx - a[i]
        rnr[i] = mx
ans = min(rp[0], lp[-1])
for i in range(1, n - 1):
    ca = lp[i - 1] + rp[i + 1]
    if max(lnr[i - 1], rnr[i + 1]) + 1 > a[i]:
        ca += max(lnr[i - 1], rnr[i + 1]) + 1 - a[i]
    ans = min(ans, ca)
print(ans)
