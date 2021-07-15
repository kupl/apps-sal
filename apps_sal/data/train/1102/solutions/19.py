# cook your dish here
t=int(input())
while(t>0):
 n=int(input())
 c=1
 while(n>0):
  m=n%10
  if(m==7 or m==9):
   c*=4
  else:
   c*=3
  n=n//10
 print(c%1000000007)
 t-=1
