# E - Roadwork
# https://atcoder.jp/contests/abc128/tasks/abc128_e

from heapq import heappop, heappush
from collections import defaultdict

n, q = list(map(int,input().split()))
task = []
for _ in range(n): 
  s, t, x = list(map(int, input().split()))
  task.append((t - x, 0, x)) 
  task.append((s - x, 1, x)) 

for i in range(q):
  d = int(input())
  task.append((d, 2, i)) 

answer = [-1] * q

task.sort()

se = set()
se_hp = []

for a, b, c in task:
  if b == 0:
    se.remove(c)
  elif b == 1:
    se.add(c)
    heappush(se_hp, c)
  else: # b == 2
    while se_hp and se_hp[0] not in se:
      heappop(se_hp)
    answer[c] = se_hp[0] if se_hp else -1

print(('\n'.join(map(str, answer))))

