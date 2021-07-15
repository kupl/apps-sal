# cook your dish here
for t in range(int(input())):
 n,k,v=map(int,input().split())
 L=list(map(int,input().split()))
 Y=((n+k)*v)-sum(L)
 if(Y>0 and Y%k==0):
  print(Y//k)
 else:
  print("-1")
