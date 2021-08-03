n, d = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
p = 0
a.sort()
i = 0
while i < n - 1:
    if a[i + 1] - a[i] <= d:
        p += 1
        i += 1
    i += 1
print(p)
