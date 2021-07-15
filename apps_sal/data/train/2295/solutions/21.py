n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr2=[]
ans=0
mb=10**18
for a,b in arr:
  ans+=a
  if a>b:
    mb=min(mb,b)
if mb==10**18:
  print(0)
else:
  print(ans-mb)
