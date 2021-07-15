N=eval(input())
while N:
 N-=1
 a,b=[int(x) for x in input().split()]
 count=0
 while a!=b:
  if b<a:
   a=a/2
   count+=1
  elif a<b:
   b=b/2
   count+=1
 print(count)
  

