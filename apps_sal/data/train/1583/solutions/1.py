t=eval(input())
for z in range(t):
 tot=0
 n,sx,sy,ex,ey,bx,by=list(map(int,input().strip().split(" ")))
 if(sx==ex or sy==ey):
  if(sx==ex):
   if(sx==bx and (by>=min(sy,ey) and by<=max(sy,ey))):
    tot+=2
  elif(sy==ey):
   if(sy==by and (bx>=min(sx,ex) and bx<=max(sx,ex))):
    tot+=2
 tot+=abs(sx-ex)+abs(sy-ey)
 print(tot)

