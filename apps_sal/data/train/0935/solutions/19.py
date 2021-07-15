n = int(input())
for i in range(n):
 ele = int(input())
 if(ele%10 == 0):
  print(0)
 else:
  ele *=2
  if(ele%10 == 0):
   print(1)
  else:
   print(-1)



