n, k, q = map(int, input().split())
b = list(map(int, input().split()))
a = sorted(b)
ans = {}
ans[a[0]] = a[0]
start = a[0]
for i in range(n - 1):
    if a[i + 1] - a[i] <= k:
        ans[a[i + 1]] = start
    else:
        start = a[i + 1]
        ans[a[i + 1]] = start
for u in range(q):
    x, y = map(int, input().split())
    if ans[max(b[y - 1], b[x - 1])] <= min(b[x - 1], b[y - 1]):
        print("Yes")
    else:
        print("No")
