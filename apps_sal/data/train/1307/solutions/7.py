t=int(input())
while(t>0):
 n,k=list(map(int,input().split()))
 j=(k**n+k*((-1) ** n))//(k+1)
 # j=(k**n+k*((-1)**n))//k+1
 #print(j)
 j=j%1000000007
 print(j)
 t-=1

