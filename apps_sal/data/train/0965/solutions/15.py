# cook your dish here
for i in range(int(input())):
 n,k=list(map(int,input().split()))
 if n==0:
  print(0,0)
 elif k==0:
  print(0,n)
 else:
  print(n//k,n%k)
   

