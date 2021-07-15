n, m = map(int,input().split())
a = list(map(int, input().split()))
l, r, ans = 0, m, m
while l <= r:
    mid = (l + r) // 2
    cur = 0 if a[0] + mid >= m else a[0]
    i = 1
    while i < n:
        if a[i] + mid < cur:
            break
        if not(a[i] < cur or (a[i] + mid >= m and (a[i] + mid) % m >= cur)):
            cur = a[i]
        i += 1
    if i == n:
        ans = min(ans, mid)
        if l == r:
            break
        r = mid
    else:
        if l == r:
            break
        l = mid + 1
print(ans)
