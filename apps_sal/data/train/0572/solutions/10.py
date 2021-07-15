# cook your dish here
n=int(input())
for i in range(n):
 n,m,k=list(map(int,input().split()))
 if n==m:
  print(0)
 elif n>m:
  c=(n-m-k)
  if c<=0:
   print(0)
  else:
   print(c)

 else:
  c=m-n-k
  if c<=0:
   print(0)
  else:
   print(c)


