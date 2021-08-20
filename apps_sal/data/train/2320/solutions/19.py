import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


m = int(input())
a = listin()
b = listin()
d = defaultdict(list)
for i in range(m):
    d[b[i]].append(i)
nums = deque(sorted(d.keys()))
a.sort(reverse=True)
a = deque(a)
ans = [0 for i in range(m)]
while nums:
    while d[nums[0]]:
        ans[d[nums[0]].pop()] = a.popleft()
    nums.popleft()
print(*ans)
