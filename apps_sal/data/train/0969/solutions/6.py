for _ in range(int(input())):
 n,k=input().split()
 laddus=0
 for j in range(int(n)):
  x=input().split()
  if x[0]=="CONTEST_WON":
   if(int(x[1])<=20):
    laddus+=300+20-int(x[1])
   else:
    laddus+=300
  elif x[0]=="TOP_CONTRIBUTOR":
   laddus+=300
  elif x[0]=="BUG_FOUND":
   laddus+=int(x[1])
  elif x[0]=="CONTEST_HOSTED":
   laddus+=50
 if(k=="INDIAN"):
  print(laddus//200)
 else:
  print(laddus//400)
