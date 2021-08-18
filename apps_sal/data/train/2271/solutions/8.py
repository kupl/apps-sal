import sys
import math
import collections
import itertools
input = sys.stdin.readline

N, M = list(map(int, input().split()))
P = list(map(int, input().split()))
bridge = [[] for i in range(N + 1)]
for _ in range(M):
    x, y = list(map(int, input().split()))
    bridge[x].append(y)
    bridge[y].append(x)
memo = [-1] * (N + 1)
q = collections.deque([])
novisit = set(range(1, N + 1))
tmp = 0
while novisit:
    q.append(novisit.pop())
    tmp += 1
    while q:
        now = q.pop()
        memo[now] = tmp
        for bri in bridge[now]:
            if bri in novisit:
                q.append(bri)
                novisit.discard(bri)
cnt = 0
for i in range(N):
    if i + 1 == P[i]:
        cnt += 1
    elif i + 1 != P[i] and memo[P[i]] == memo[i + 1]:
        cnt += 1
print(cnt)
