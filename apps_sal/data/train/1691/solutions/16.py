import sys
import numpy as np


def find_nearest(array, value):
    idx = np.abs(array - value).argmin()
    return array[idx]


(n, m, c) = list(map(int, input().split()))
max = []
li = []
options = []
for i in range(1, 6):
    print(1, 1, n, 1, m, i, i)
    sys.stdout.flush()
    ans = int(input())
    max.append(ans)
    li.append(ans)
max.sort()
max = max[::-1]
for i in range(5):
    options.append(li.index(max[i]) + 1)
array = np.array(options)
k = 1
li = []
query = m
rem = 0
if c <= query:
    query = c
    rem = m - query
for i in range(query):
    print(2, 1, n, k, k + 1 - 1)
    sys.stdout.flush()
    sum = int(input())
    li.append(sum / n)
    if k >= m:
        break
    k += 1
print(3)
for i in range(n):
    for j in range(query):
        print(str(find_nearest(array, li[j])), end=' ')
    print(' '.join([str(options[0])] * rem))
