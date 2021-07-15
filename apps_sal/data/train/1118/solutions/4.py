for i in range(int(input())):
 n=int(input())
 l=input()
 k=n//2
 p='10'*k
 q='01'*k
 x=y=0
 if n%2==0:
  for i in range(n):
   if l[i]!=p[i]:
    x=x+1
   if l[i]!=q[i]:
    y=y+1
  print(min(x,y))
 else:
  p=p+'1'
  q=q+'0'
  for i in range(n):
   if l[i]!=p[i]:
    x=x+1
   if l[i]!=q[i]:
    y=y+1
  print(min(x,y))
 


