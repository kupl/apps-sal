# cook your dish here
t=int(input())
for _ in range(t):
 a=int(input())
 l=list(map(int,input().split()))
 l1=sorted(l)
 if len(l)==1:
  print(l[0])
 elif len(l)==2:
  print(max(l1[1],l1[0]))
 else:
  x=0
  k=l1[0]+l1[1]
  for i in range(2,len(l1)):
   x=x+(l1[i]-l1[i-1])
  print(k+x)
  
  

