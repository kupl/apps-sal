t=int(input())
for i in range(t):
 n=int(input())
 ans=0
 for j in range(2,n,2):
  if int((n**2-j**2)**0.5)==(n**2-j**2)**0.5:
   ans=ans or 1
   break
  else:
   ans=ans or 0
 if ans==1:
  print("YES")
 else:
  print("NO")


