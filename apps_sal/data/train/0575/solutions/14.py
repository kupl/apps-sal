for _ in range(int(input())):
 q=input()
 x=0
 o=0
 y=[]
 z=-1
 c=-1
 for ii in range(len(q)):
  if(q[ii]!='='):
   y.append(q[ii])
 for i in range(len(y)):
  if(y[i]=='>')and(o==0):
   x+=1
  elif(y[i]=='<')and(x==0):
   o+=1
  else:
   if(z<o):
    z=o
   if(c<x):
    c=x
   if(y[i]=='>'):
    x=1
    o=0
   if(y[i]=='<'):
    o=1
    x=0
 if(z<o):
  z=o
 if(c<x):
  c=x
 print(max(z,c,0)+1)

