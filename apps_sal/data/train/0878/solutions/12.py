for _ in range(int(input())):
 Ans=0
 N,K=map(int,input().split())
 H=list(map(int,input().split()))
 for i in range(N):
  if i==0 and K<H[i]:
   Ans=Ans+(H[i]-1)//K
  elif K<H[i]-H[i-1] and i>0:
   Ans=Ans+(H[i]-H[i-1]-1)//K
 print(Ans)
