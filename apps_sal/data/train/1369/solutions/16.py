def isprime(n):
 if n==2:
  return 1
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   return 0
 return 1 
t=int(input())
for z in range(t):
 n=int(input())
 s=0
 for i in range(2,n+1):
  if isprime(i):
   s+=i
 print(s) 

