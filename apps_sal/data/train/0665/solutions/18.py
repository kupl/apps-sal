# cook your dish here
import sys

t=int(input())
for _ in range(t):
 N,M= list(map(int,input().split()))
 C=[[0 for x in range(N)]for y in range(M+1)]
 C[0] = list(map(int,input().split()))

 rating=[0 for x in range(N)]
 rank = [sys.maxsize for x in range(N)]

 for i in range(N):
  change=list(map(int,input().split()))
  rate = 0
  month = 0
  for j in range(1,M+1):
   C[j][i]=C[j-1][i]+change[j-1]
   if C[j][i] > rate:
    rate=C[j][i]
    month=j

  rating[i]=month


 mon=[0 for x in range(N)]
 for i in range(1,M+1):
  X=sorted(C[i],reverse=True)
  for j in range(N):
   temp=X.index(C[i][j])
   if temp < rank[j] :
    rank[j]=temp
    mon[j]=i

 pl=0
 for i in range(N):
  if mon[i]==rating[i]:
   pl+=1

 print(N-pl)










