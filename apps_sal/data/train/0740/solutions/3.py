from sys import stdin
def sin():
 return stdin.readline()

for _ in range(int(sin())):
 n,m,k = list(map(int, sin().split()))
 d={}
 ans=4*k
 for i in range(k):
  r,c = list(map(int, sin().split()))
  ans-=(2*d.get((r-1,c),0)+
   2*(d.get((r,c-1),0))+
   2*(d.get((r+1,c),0))+
   2*(d.get((r,c+1),0)))
  d[r,c]=1
 print(ans)

