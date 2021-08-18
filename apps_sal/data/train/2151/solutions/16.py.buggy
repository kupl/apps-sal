n, s = map(int, input().split())
z = list(map(int, input().split()))
z.sort()
y = n // 2
c = 0
if z[y] == s:
    print(c)
    return
if z[y] < s:
    for i in range(y, n):
        if z[i] < s:
            c += s - z[i]
else:
    for i in range(0, y + 1):
        if z[i] > s:
            c += z[i] - s
print(c)
