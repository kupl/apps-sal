t=int(input())
for i in range(t):
 n=int(input())
 a=input().split()
 b=set(a)
 ma=0
 for j in b:
  p=a.count(j)
  if(ma<p):
   ma=p
 print(n-ma)
