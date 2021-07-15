import bisect
import math
N = int(input())
x = list(map(int, input().split()))
L = int(input())

m = int(math.log(max(x), 2) + 1)
#i番目のホテルから2 ** k 日以内に到達可能な
#もっとも右にあるホテル
r = [[-1] * N for k in range(m)]
for i in range(N):
  base = x[i] + L
  p = bisect.bisect_right(x, base)
  #print(p)
  r[0][i] = p - 1

#ダブリング
for k in range(m - 1):
  for i in range(N):
    r[k + 1][i] = r[k][r[k][i]]
#print(r)    
   
def isOK(mid):
  now = a
  pp = int(math.log(mid, 2) + 1)
  for i in range(pp):
    if (mid >> i) & 1:
      now = r[i][now]
      #print(now, a + 1, b + 1, mid)
  if now >= b:
    return True
  else:
    return False
  
Q = int(input())
for i in range(Q):
  a, b = list(map(int, input().split()))
  a, b = a-1, b-1
  if a > b:
    a, b = b, a
  ng = 0
  ok = 2 ** m
  while (abs(ok - ng) > 1):
    mid = int((ok + ng) / 2)
    #print(mid)
    if isOK(mid):
      ok = mid
    else:
      ng = mid
  print(ok)
         

         
         

