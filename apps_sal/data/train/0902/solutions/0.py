for u in range(int(input())):
 p=input().split()
 n=int(p[0])
 s=p[1]
 x,y=0,0
 for i in range(n):
  l=input()
  if(l[0]=='1'):
   y+=l.count('1')
  else:
   x+=l.count('0')
 if(x<y):
  print("Dum")
 elif(y<x):
  print("Dee")
 else:
  if(s=='Dee'):
   print("Dum")
  else:
   print("Dee")

