from collections import *
for t in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 c = Counter()
 for e in a:
  c[e] += 1
 for k,v in sorted(c.items()):
  print(str(k)+':', v)

