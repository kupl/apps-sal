from fractions import gcd as G
for ii in range(eval(input())):
 n=eval(input())
 arr=list(map(int,input().split()))
 k=arr[0]
 for i in range(1,n-1):
  k=G(k,arr[i])
 print(k*n)
  
  

