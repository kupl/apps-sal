n, m = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, m - 1
while l < r:
    mid = (l + r) // 2
    p = 0
    f = True
    for x in arr:
        step = (m - x + p) % m
        if step > mid:
            if x < p:
                f = False
                break
            p = x
    if f is True:
        r = mid
    else:
        l = mid + 1
print(l)
