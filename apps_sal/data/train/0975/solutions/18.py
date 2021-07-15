t=int(input())
for _ in range(t):

 n,r,nx,ny=list(map(int,input().split()))
 if nx>0:
  x=set(map(int,input().split()))
#        x=list(range(500000))
 else:
  x=set()
 if ny>0:
  y=set(map(int,input().split()))
#        y=list(range(1000000))
 else:
  y=set()

 common=len(set.intersection(x,y))

 genuine_c=n-nx-ny+common

 if genuine_c>r:
  print(r)
 else:
  print(genuine_c)

