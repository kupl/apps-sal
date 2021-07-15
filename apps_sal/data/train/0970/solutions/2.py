# cook your dish here
import bisect
test=int(input())
for _ in range(test):
 n=int(input())
 ls=list(map(int,input().split()))
 ls.sort()
 q=int(input())
 for _ in range(q):
  x,y=map(int,input().split())
  z=x+y
  m=bisect.bisect(ls,z)
  if m>0:
   if ls[m-1]==z:
    print(-1)
   else:
    print(m)
  else:
   print(0)
