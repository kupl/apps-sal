n = int(input())
arr = [int(input()) for i in range(n)]
b = [0 for i in range(n)]
s = 0
for i in range(n):
    j = int((arr[i] << 1) ** 0.5)
    if j * (j + 1) > (arr[i] << 1):
        j -= 1
    s ^= j
if s != 0:
    print('NO')
else:
    print('YES')
