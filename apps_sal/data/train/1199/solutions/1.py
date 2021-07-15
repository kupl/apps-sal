for i in range(int(input())):
 n,k=map(int,input().split())
 t=0
 if n%2!=0:
  n-=1
  t+=1
 t+=(n//k)
 if n%k!=0:
  t+=1
 print(t)
