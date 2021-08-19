import sys
import math
from collections import defaultdict, deque
import heapq

n, k = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
st = 2
q = deque()
for i in range(k):
    graph[1].append(st)
    q.append(st)
    st += 1
leaves = [1 for _ in range(k)]
cnt = 0
while q and st <= n:
    a = q.popleft()
    graph[a].append(st)
    q.append(st)
    leaves[(cnt) % k] += 1
    cnt += 1
    st += 1
# print(leaves,'leaves')
dis = leaves[0] + leaves[1]
leaves.sort()
dis = leaves[-1] + leaves[-2]
q = deque()
q.append(1)
vis = defaultdict(int)
print(dis)
while q:
    a = q.popleft()
    for x in graph[a]:
        print(a, x)
        q.append(x)
