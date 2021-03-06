from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy
N = int(input())
arr = [int(x) for x in stdin.readline().split()]
bit = [0] * N
series = [x for x in range(N)]


def lowbit(x):
    return x & -x


def update(idx, delta):
    while idx < N:
        bit[idx] += delta
        idx += lowbit(idx)


def query(x):
    s = 0
    while x > 0:
        s += bit[x]
        x -= lowbit(x)
    return s


for i in range(N):
    bit[i] += series[i]
    y = i + lowbit(i)
    if y < N:
        series[y] += series[i]
visited = [0] * N
ans = [0] * N
for i in range(N - 1, -1, -1):
    left = 0
    right = N - 1
    target = arr[i]
    while left <= right:
        mid = (left + right) // 2
        q = query(mid)
        if q < target:
            left = mid + 1
        elif q > target:
            right = mid - 1
        elif visited[mid] == 1:
            left = mid + 1
        else:
            visited[mid] = 1
            ans[i] = mid + 1
            break
    if mid + 1 < N:
        update(mid + 1, -mid - 1)
print(*ans)
