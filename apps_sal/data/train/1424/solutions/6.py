# cook your dish here
n,k=map(int,input().split())
while n!=1 and k:
 if n%10==0:
  n//=10
 else:
  n-=1
 k-=1
print(n)
