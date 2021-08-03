import random
n = int(input())
a = list(map(int, input().split(' ')))
c = 0
for i in range(1, n + 1):
    if a[i - 1] == i:
        c += 1

if c >= n // 1000:
    print("Petr")
else:
    print("Um_nik")
