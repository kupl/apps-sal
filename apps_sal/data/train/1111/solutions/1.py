t=int(input()) 
for kkk in range(t): 
 n=int(input()) 
 a=[int(x) for x in input ().split()] 
 e=0
 o=0
 for i in range(n): 
  if a[i]%2==0: 
   e+=1
  else: 
   o+=1
 print(e*o)

