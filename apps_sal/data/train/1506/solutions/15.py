import math
from collections import defaultdict
import sys
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


n, m = get_ints()
a = []
arr = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
for _ in range(n):
    t = list(input())
    a.append(t)

for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])


q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = get_ints()
    arr[x1][y1] += 1
    arr[x2 + 1][y2 + 1] += 1
    arr[x1][y2 + 1] -= 1
    arr[x2 + 1][y1] -= 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
        if(a[i - 1][j - 1] == 0 and arr[i][j] % 2 == 0):
            a[i - 1][j - 1] = 0
        elif(a[i - 1][j - 1] == 1 and arr[i][j] % 2 == 0):
            a[i - 1][j - 1] = 1
        elif(a[i - 1][j - 1] == 0 and arr[i][j] % 2 == 1):
            a[i - 1][j - 1] = 1
        elif(a[i - 1][j - 1] == 1 and arr[i][j] % 2 == 1):
            a[i - 1][j - 1] = 0


for i in range(n):
    print(''.join(map(str, a[i])))
