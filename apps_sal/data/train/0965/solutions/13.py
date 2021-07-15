# cook your dish here
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 if k==0:
  print(0,n)
 else:
  print(n//k,n%k)

