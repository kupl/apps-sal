for t in range(int(input())):
 ls = list(input())
 flag1 = 0
 for i in range(1,len(ls)):
  if ord(ls[i])>=ord(ls[i-1]):
   continue
  else:
   flag1 = 1 
   break
 if flag1 == 0:
  print("yes")
 else:
  print("no")
