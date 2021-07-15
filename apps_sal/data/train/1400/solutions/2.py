for _ in range(int(input())):
 n,l,r=list(map(int,input().split()))
 s=0
 mi=0
 ma=0
 for i in range(l):
  mi+=pow(2,i)
 mi+=n-l
 for i in range(r):
  ma+=pow(2,i)
 ma+=(n-r)*(pow(2,r-1))
 print(mi,ma)


