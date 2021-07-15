t=int(input())
for x in range(t):
 a=input()
 b=input()
 flag=False
 for i in a:
  if i in b:
   flag=True
   break
 if flag :
  print("Yes")
 else:
  print("No")
  


