n=int(input())
for i in range(n):
 m=int(input())
 a=""
 b="1"
 p=65
 q=2
 for j in range(m):
  if j%2==0:
   a=a+chr(p)
   print(a)
   p+=1
   a=a+chr(p)
   p+=1
  else:
   b=b+str(q)
   print(b)
   q=q+1
   b=b+str(q)
   q=q+1
