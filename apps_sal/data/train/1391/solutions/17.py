# find disjoint intervals

from collections import defaultdict
for _ in range(int(input())):
 n, k = list(map(int, input().strip().split()))

 times = defaultdict(list)

 for i in range(n):
  start, finish, p = [int(x) for x in input().strip().split()]
  times[p].append((start, finish))

 ans = 0

 # print(times)
 for c in list(times.values()):
  c.sort(key = lambda x: x[1])
  finish_time = 0
  for st, ft in c:
   if st >= finish_time:
    ans += 1
    finish_time = ft 
 print(ans)

