import math
n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
low = a[0]
high = sum(a)
while low < high:
    mid = (low + high) // 2
    t = 0
    i = 0
    while i < n and t < mid:
        if t >= a[i]:
            t = mid
            break
        t += mid - a[i]
        i += 1
    if t >= mid:
        high = mid
    else:
        low = mid + 1
print(high)
