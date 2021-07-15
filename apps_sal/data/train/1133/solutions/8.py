# cook your dish here
try:
 def find_gcd(x, y): 
  
  while(y): 
   x, y = y, x % y 
   
  return x 
 for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  if n==1:
   print(l[0],1)
   continue
  g=find_gcd(l[0],l[1])
  for i in range(2,n):
   g=find_gcd(g,l[i])
  s=0
  for i in l:
   s+=i/g
  print(g,int(s))
except:pass 
