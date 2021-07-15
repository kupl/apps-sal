# cook your dish here
import bisect
for _ in range(int(input())):
 N,Q=list(map(int,input().strip().split(' ')))
 V=list(map(int,input().strip().split(' ')))
 VV=sorted(V)
 for ___ in range(Q):
  x,y=list(map(int,input().strip().split(' ')))
  x-=1
  y-=1
  ans1=abs(V[x]-V[y])+(y-x)
  post1=bisect.bisect_left(VV,min(V[x],V[y]))
  post2=bisect.bisect_right(VV,max(V[x],V[y]))
  ans2=post2-post1
  print(ans1,ans2)

