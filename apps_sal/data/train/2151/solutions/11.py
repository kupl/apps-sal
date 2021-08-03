n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
x = n // 2
c = 0
if a[x] == s:
    print(c)
    return
if a[x] < s:
    for i in range(x, n):
        if a[i] < s:
            c += s - a[i]
else:
    for i in range(0, x + 1):
        if a[i] > s:
            c += a[i] - s
print(c)
