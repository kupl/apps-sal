m = int(input())
q = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
mn = min(q)
a.sort(reverse=True)
(ans, p) = (0, 0)
while 1:
    for i in range(p, min(p + mn, n)):
        ans += a[i]
    p += mn + 2
    if p >= n:
        break
print(ans)
