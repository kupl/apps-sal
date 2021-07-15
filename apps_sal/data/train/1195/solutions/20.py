from sys import stdin, stdout
from math import gcd
ans = []

for _ in range(int(stdin.readline())):
 n, a, b, c, d, p, q, y = list(map(int, stdin.readline().split()))
 nArr = list(map(int, stdin.readline().split()))
 wT = abs((nArr[b - 1] - nArr[a - 1]) * p)
 WTTT = abs((nArr[c - 1] - nArr[a - 1]) * p)
 if WTTT > y:
  ans.append(str(wT))
  continue
 tT = abs((nArr[c - 1] - nArr[d - 1]) * q)
 tTBCT = abs((nArr[d - 1] - nArr[b - 1]) * p)
 vTT = y + tT + tTBCT
 ans.append(str(wT) if wT < vTT else str(vTT))
stdout.write('\n'.join(ans))

