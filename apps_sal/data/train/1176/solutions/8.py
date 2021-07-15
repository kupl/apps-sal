for i in range(int(input())):
 s=input()
 l=list(s)
 if(len(l)>=4):
  if(s[-4:]=="1000"):
   print("YES")
  else:
   print("NO")
 else:
  print("NO")
