n, m, k = list(map(int, input().split()))
a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()), reverse=True)
cou = ind = 0
l = min(m, n)
aa = max(b)
for i in range(l):
    if a[i] > b[i]:
        cou += 1
        ind = max(ind, a[i])

if m >= n and cou > 0:
    print("YES")
elif m < n:
    print("YES")
else:
    print("NO")
