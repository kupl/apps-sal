n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
mn = a[0]
l = []
for i in range(n - 1):
    if a[i] < a[i + 1]:
        l.append(a[i + 1] - mn)
    if a[i + 1] < mn:
        mn = a[i + 1]
if len(l) > 0:
    d = max(l)
ans = l.count(d)
print(ans)
