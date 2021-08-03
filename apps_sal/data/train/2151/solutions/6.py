n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

mid = n // 2

a.sort()
res = 0
median = a[mid]

j = mid

if median < s:
    while j < n and a[j] < s:
        res += s - a[j]
        j += 1
elif median > s:
    while j >= 0 and a[j] > s:
        res += a[j] - s
        j -= 1


print(res)
