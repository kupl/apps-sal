from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy
N = int(input())
arr = [int(x) for x in stdin.readline().split()]
bit = [0] * (N + 1)
series = [0] + [x for x in range(N)]


def lowbit(x):
    return x & -x


def update(idx, delta):
    while idx <= N:
        bit[idx] += delta
        idx += lowbit(idx)


def query(x):
    s = 0
    while x > 0:
        s += bit[x]
        x -= lowbit(x)
    return s


for i in range(1, N + 1):
    bit[i] += series[i]
    y = i + lowbit(i)
    if y <= N:
        series[y] += series[i]
visited = [0] * (N + 1)
ans = [0] * N
for i in range(N - 1, -1, -1):
    left = 1
    right = N
    target = arr[i]
    while True:
        L = right - left + 1
        num = left - 1 + 2 ** int(math.log(L, 2))
        q = bit[num]
        if q < target:
            target -= q
            left = num + 1
        elif q > target:
            right = num - 1
        elif visited[num] == 1:
            target -= q
            left = num + 1
        else:
            visited[num] = 1
            ans[i] = num
            break
    update(num + 1, -num)
print(*ans)
