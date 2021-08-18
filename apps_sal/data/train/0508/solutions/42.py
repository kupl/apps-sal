from heapq import heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

N, Q = list(map(int, input().split()))
task = []

STX = [[int(x) for x in input().split()] for _ in range(N)]
for s, t, x in STX:
    task.append((t - x, 0, x))
    task.append((s - x, 1, x))

for i in range(Q):
    d = int(input())
    task.append((d, 2, i))
answer = [-1] * Q

task.sort()

se = set()
se_hp = []

for a, b, c in task:
    if not b:
        se.remove(c)
    elif b & 1:
        se.add(c)
        heappush(se_hp, c)
    else:
        while se_hp and se_hp[0] not in se:
            heappop(se_hp)
        answer[c] = se_hp[0] if se_hp else -1

print(('\n'.join(map(str, answer))))
