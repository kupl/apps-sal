n = int(input())
arr = list(map(int, input().split()))
arr.sort()
(a, b, c) = (0, 0, 0)
temp = 1
for i in range(n - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        a = arr[i + 2]
        b = arr[i + 1]
        c = arr[i]
        temp = 0
if temp == 1:
    print('NO')
else:
    print('YES')
    print(a, b, c)
