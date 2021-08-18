
from random import *

n, m, c = list(map(int, input().split()))
print(3)
arr = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = randint(1, 50)

for a in arr:
    print(' '.join(map(str, a)))
