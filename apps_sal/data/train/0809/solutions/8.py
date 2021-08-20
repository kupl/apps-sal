n = int(input())
a = list(map(int, input().split()))
a.sort()
i = n - 3
ans = []
tmp = 0
while i >= 0:
    if a[i] + a[i + 1] > a[i + 2]:
        print('YES')
        print(a[i + 2], a[i + 1], a[i])
        tmp = 1
        break
    i -= 1
if tmp == 0:
    print('NO')
