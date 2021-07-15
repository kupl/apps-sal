# cook your dish here
t=int(input())
for _ in range(t):
 x1,y1,x2,y2=map(int,input().split())
 x3,y3,x4,y4=map(int,input().split())
 if (x1==x3 and y1==y3)or(x2==x4 and y2==y4):
  print("yes")
 elif (x1==x4 and y1==y4)or(x2==x3 and y2==y3):
  print("yes")
 else:
  if(y1==y2)and(y1==y3)and(y1==y4):
   a1=max(x1,x2);a2=min(x1,x2)
   b1=max(x3,x4);b2=min(x3,x4)
   if a1>=b2 and a2<=b1:
    print("yes")
   else:
    print("no")
  elif (x1==x2)and(x1==x3)and(x1==x4):
   a1=max(y1,y2);a2=min(y1,y2)
   b1=max(y3,y4);b2=min(y3,y4)
   if a1>=b2 and a2<=b1:
    print("yes")
   else:
    print("no")
  else:
   print("no")
