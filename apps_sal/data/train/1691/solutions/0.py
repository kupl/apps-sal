
import sys
from random import *

n, m, c = list(map(int, input().split()))
arr = [[1] * m for i in range(n)]
saved = 0
for i in range(n):
    for j in range(m):
        print(1, (i + 1), (i + 1), (j + 1), (j + 1), 1, 25)
        sys.stdout.flush()
        a = int(input())
        if a == 1:
            saved += 1
            arr[i][j] = randint(1, 25)
        else:
            arr[i][j] = randint(25, 50)
print(3)
sys.stdout.flush()
for a in arr:
    print(' '.join(map(str, a)))
    sys.stdout.flush()
