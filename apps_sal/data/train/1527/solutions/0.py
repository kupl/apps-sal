for j in range(int(input())):
 a=input()
 b=input()
 c,d=0,0
 a0=a.count("0")
 a1=a.count("1")
 if(a0==len(a) or a1==len(a)):
  print("Unlucky Chef")
 else:
  print("Lucky Chef")
  for i in range(len(a)):
   if(a[i]!=b[i]):
    if(a[i]=="0"):
     c+=1
    else:
     d+=1
  print(max(c,d))
