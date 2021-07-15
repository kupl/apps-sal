t=int(input())
c=0
while (t):
 n=int(input())
 for i in range(1,n):
  if n%i==0:
   c+=1
 
 if c%2==0:
  print("YES\n")
 else:
  print("NO\n")
 c=0
 t=t-1
