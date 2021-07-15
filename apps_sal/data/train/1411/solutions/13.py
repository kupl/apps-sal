# cook your dish here
try:
 t=int(input())
 for _ in range(t):
  x,r,A,B=map(int,input().split())
  if(A<B):
   A,B=B,A
  q=2*(22/7)*r
  t=(q/abs(A-B))*A
  d=x*q
  ans=d/t
  if(ans==int(ans)):
   print(int(ans)-1)
  else:
   print(int(ans))
except:
 pass
