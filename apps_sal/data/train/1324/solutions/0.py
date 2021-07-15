from math import sqrt

for _ in range(int(input())):
 
 n, k = map(int, input().split())
 fact,i = [],1
 
 while i<=sqrt(n):

  if n%i==0:
   if (n // i != i):
    fact.append(n//i)
   
   fact.append(i)
   
  i+=1
  
 tot = (k*(k+1))//2
 mx = -1
 
 for i in fact:
  if i>=tot:
   mx = max(mx,n//i)
   
 print(mx)
