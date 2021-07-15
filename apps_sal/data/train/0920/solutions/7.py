from itertools import permutations as p
t=int(input())
for _ in range(t):
 s=input()
 
 a=s.count('b')
 b=s.count('g')
 if a==0 or b==0:
  print(0)
  continue
 if a<=b:
  k=b-a+1
  x=k//2
  y=k//2
  if k%2:
   x+=1
  s='g'*x
  for i in range(a-1):
   s+='b'
   s+='g'
  s+='b'
  s+='g'*y

 else:
  temp=a
  a=b
  b=temp
  
  k=b-a+1
  x=k//2
  y=k//2
  if k%2:
   x+=1
  s='g'*x
  for i in range(a-1):
   s+='b'
   s+='g'
  s+='b'
  s+='g'*y

 ans=0
 n=len(s)
 g=0
 b=0
 countg=0
 countb=0
 for i in range(n-1,-1,-1):
  if s[i]=='g':
   ans+=b-i*countb
   g+=i
   countg+=1
  else:
   ans+=g-i*countg
   b+=i
   countb+=1
 print(ans)
   
  

