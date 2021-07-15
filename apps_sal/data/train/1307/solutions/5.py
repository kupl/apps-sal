t=int(input())
while(t>0):
 n,k=map(int,input().split())
 j=(k**n+k*((-1) ** n))//(k+1)

 j=j%1000000007
 print(j)
 t-=1
