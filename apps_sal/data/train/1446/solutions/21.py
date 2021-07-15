for i in range(int(input())):
 n=int(input())
 t=-1
 for j in range(30):
  if n==2**j-1:
   t=j
   break
 if t==1:
  print(2)
 elif t==-1:
  print(-1)
 else:
  print(2**(t-1)-1)

