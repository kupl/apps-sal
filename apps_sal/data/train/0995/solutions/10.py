n = int(input())
a = list(map(int, input().split()))
k = int(input())
ws = 0
mws = 0
l = k - 1
r = n - 1
if k == n:
    print(sum(a))
elif k == n - 1:
    print(sum(a) - min(a))
else:
    for x in range(k):
        ws = ws + a[x]
    mws = ws
    while l >= 0:
        ws = ws - a[l] + a[r]
        l = l - 1
        r = r - 1
        if mws < ws:
            mws = ws
    print(mws)
