t = int(input())
for _ in range(t):
 n = int(input())
 s = [int(i) for i in input().split()]
 x = []
 c = 0
 for i in range(n):
  x.append(s[i])
  
 for i in range(n-1):
  if x[i]<x[i+1]:
   x[i+1]=x[i]
 
 for i in range(n):
  if s[i]==x[i]:
   c+=1
 
 print(c)
 

