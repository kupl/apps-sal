n = int(input())

a = list(map(int, input().strip()))
b = list(map(int, input().strip()))

res = 0

for j in range(n - 1):
    if (a[j] == 0) and (a[j + 1] == 1) and (b[j] == 1) and (b[j + 1] == 0):
        res += 1
        a[j] = 1
        a[j + 1] = 0

    elif (a[j] == 1) and (a[j + 1] == 0) and (b[j] == 0) and (b[j + 1] == 1):
        res += 1
        a[j] = 0
        a[j + 1] = 1

for j in range(n):
    if a[j] != b[j]:
        res += 1

print(res)
