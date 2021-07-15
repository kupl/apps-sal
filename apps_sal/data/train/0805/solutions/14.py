import math
T = int(input())
for _ in range(T):
 n = int(input())
 #s = []
 #v = []
 #p = []
 m = -1
 for i in range(n):
  si,pi,vi = map(int,input().split())
  si = si + 1
  #s.append(si)
  #v.append(vi)
  #p.append(pi)
  dailyProfit = vi*(math.floor(pi/si))
  #print(si,vi,pi,dailyProfit,m)
  if dailyProfit>m:
   m = dailyProfit
 print(m)
