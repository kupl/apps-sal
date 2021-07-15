n=int(input())
total=0
allsame=1
minb=10**9+1
for _ in range(n):
  a,b=list(map(int,input().split()))
  total+=a
  if a>b:
    allsame=0
    minb=min(b,minb)
if allsame==1:
  print((0))
else:
  print((total-minb))

