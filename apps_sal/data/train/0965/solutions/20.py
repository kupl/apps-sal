# cook your dish here
t=int(input())
while t>0:
 n,k=map(int,input().split())
 if k==0:
  print(0,n)
 else:
  c=n//k
  q=n%k
  print(c,q)
 t=t-1
