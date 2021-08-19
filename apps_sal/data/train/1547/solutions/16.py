(d1, v1, d2, v2, n) = map(int, input().split())
(l, i, j, day) = (0, 1, 1, 0)
while l < n:
    if i >= d1:
        l += v1
    if j >= d2:
        l += v2
    i += 1
    j += 1
    day += 1
print(day)
