n = int(input())
a = list(input())
b = list(input())

cnt = 0

for i in range(n - 1):
    if (a[i] == b[i + 1]) and (a[i + 1] == b[i]) and (a[i] != a[i + 1]):
        cnt += 1
        a[i], a[i + 1] = a[i + 1], a[i]

for i in range(n):
    if a[i] != b[i]:
        cnt += 1

print(cnt)
