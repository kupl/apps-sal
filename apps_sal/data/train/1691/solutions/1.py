
import sys
from random import *

n, m, c = list(map(int, input().split()))
arr = [[1] * m for i in range(n)]
saved = 0
for i in range(n):
    for j in range(m):
        print(1, (i + 1), (i + 1), (j + 1), (j + 1), 1, 15)
        sys.stdout.flush()
        a = int(input())
        if a == 1:
            saved += 1
            arr[i][j] = randint(1, 15)
        else:
            print(1, (i + 1), (i + 1), (j + 1), (j + 1), 16, 30)
            sys.stdout.flush()
            a = int(input())
            if a == 1:
                arr[i][j] = randint(16, 30)
            else:
                if saved > 0:
                    saved -= 1
                    print(1, (i + 1), (i + 1), (j + 1), (j + 1), 31, 40)
                    sys.stdout.flush()
                    a = int(input())
                    if a == 1:
                        arr[i][j] = randint(31, 40)
                    else:
                        arr[i][j] = randint(41, 50)
                else:
                    arr[i][j] = randint(31, 50)
print(3)
sys.stdout.flush()
for a in arr:
    print(' '.join(map(str, a)))
    sys.stdout.flush()
