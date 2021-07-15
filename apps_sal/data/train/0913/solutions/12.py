import sys
import statistics 
from statistics import mode
readline = sys.stdin.readline
try:
  
 INF = 10**18+3
 N, M, K = map(int, readline().split())
 Points = [tuple(map(int, readline().split())) for _ in range(K)]
 ABC = [(p[1], p[3], abs(p[0] - p[2])) for p in Points]
 ans = INF
 l=[]
 if K <= 10:
  ans = INF
  for m in range(1, M+1):
   res = 0
   for a, b, c in ABC:
    res += min(2*abs(a-m) + 2*abs(b-m) + c, 2*abs(a-b) + 2*c)
   ans = min(ans, res)
  print(ans)
 else:
  def horiz():
   ans=0
 
   for yo,y1,x in ABC:
     max1=0
     lv=1
     dist=[0]*M
     if (yo-x//4)>1:
      lv=yo-x//4
     up=M
     if (x//4+y1)<up:
      up=x//4+y1
     for j in range(lv,up+1):
      if j < yo:
       dist[j]+=x-4*(yo-j)
      elif j>=yo and j<=y1:
       dist[j]+=x
      else:
       dist[j]+=x-4*(j-y1)
      if dist[j]>dist[max1]:
       max1=j
     return dist[max1]
 

  m = horiz()
  res = 0
  for a, b, c in ABC:
   res += (2*abs(a-b) +2*c)
  print(ans-m)
except:
 pass
