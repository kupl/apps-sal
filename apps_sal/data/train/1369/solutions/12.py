try:
 def solver(n):
  prime = [True for i in range(n+1)]
  p = 2
  while(p*p<=n):
   if(prime[p]==True):
    for i in range(p*2,n+1,p):
     prime[i] = False
   p+=1
  prime[0]= False
  prime[1] = False
  s = 0
  for i in range(n+1):
   if(prime[i]):
    s+=i
  return s 
  
 t = int(input())
 for i in range(t):
  n = int(input())
  print(solver(n))
  
 
 
 
except Exception as e:
 pass
