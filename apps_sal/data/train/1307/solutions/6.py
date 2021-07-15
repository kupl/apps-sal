# cook your dish here
t=int(input())
for i in range(t):
 n,k=list(map(int,input().split(" ")))
 sum=0
 z=0
 while(n>1):
  sum+=(k**(n-1))*((-1)**z)
  n-=1
  z+=1
 print(sum%1000000007)


