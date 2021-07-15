from bisect import bisect
N=int(input())
X=[int(x) for x in input().split()]
L=int(input())
inf=float("inf")
X.append(X[-1]+L)
Table=[[inf]*18 for i in range(N)]
r=1
for i in range(N):
  if r<=N:
    while X[r]-X[i]<=L:
      r+=1
      if r>N:
        break
  Table[i][0]=r-1
for k in range(1,18):
  for i in range(N):
    if Table[i][k-1]==N:
      Table[i][k]=N
      continue
    Table[i][k]=Table[Table[i][k-1]][k-1]

Q=int(input())
for q in range(Q):
  a,b=list(map(int,input().split()))
  a-=1
  b-=1
  ans=0
  if a>b:
    a,b=b,a
  while a<b:
    i=bisect(Table[a],b)-1
    if i>=0:
      ans+=2**i
    else:
      ans+=1
    a=Table[a][i]
  
  print(ans)

