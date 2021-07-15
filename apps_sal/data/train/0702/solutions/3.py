# cook your dish here
try:
 t=int(input())
 for _ in range(t):
  m,a,b=map(int,input().split())
  if (b-a)%3==0 and(b-a)/3<=m :
   print("No")
  else:
   print("Yes")
   
except:
 pass
