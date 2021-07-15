import sys
def revsubseq(lis):
 s = 0 ; e = n - 1
 nls = []
 while e > s:
  if lis[s] > 0 and lis[e] <= 0:
   lis[s], lis[e] = lis[e], lis[s]
   nls.append(s + 1)
   nls.append(e + 1)
   s+=1 ; e-=1
  elif lis[s] <= 0 and lis[e] > 0:
   s+=1 ; e-=1
  elif lis[s] <= 0 and lis[e] <= 0:
   s+=1
  elif lis[s] > 0 and lis[e] > 0:
   e-=1
 return nls

def mxsubarray(lis):
 globalmax = lis[0] ; curmax = lis[0]
 for i in range(1, n):
  curmax = max(curmax + lis[i], lis[i])
  globalmax = max(globalmax, curmax)
 return globalmax

for t in range(int(input())):
 n = int(input())
 lis = list(map(int, input(). split()))
 nls = revsubseq(lis)
 mx = mxsubarray(lis)
 if mx < 0:
  print(0)
  print(0)
 else:
  print(mx)
  print(len(nls), end = ' ')
  print(*nls)
