t=int(input())
for each in range(t):
 x,y=map(int,input().split())
 if x>y:
  if (x-y)%2==0:
   print("1")
  else:
   print("2")
 elif x<y:
  if (y-x)%2!=0:
   print("1")
  elif (y-x)%2==0 and (y-x)%4!=0:
   print("2")
  else:
   print("3")
 else:
  print("0")
