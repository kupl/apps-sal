# cook your dish here
for _ in range(int(input())):
 x,y = map(int,input().split())
 if x == y:
  print(0)
 elif x > y:
  if (x-y)%2==0:
   print(1)
  else:
   print(2)
 else:
  if (y-x)%4 == 0:
   print(3)
  elif (y-x)%2 == 0:
   print(2)
  else:
   print(1)
