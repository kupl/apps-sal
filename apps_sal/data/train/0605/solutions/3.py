for _ in range(int(input())):
 n,m=map(int,input().split())
 s=input()
 t1,t2,t3,t4=0,0,0,0
 # d={'L':0,'R':1,'U':2,'D':3}
 # l=[0,0,0,0]
 xp,xn,yp,yn=0,0,0,0
 c1,c2=0,0
 for i,x in enumerate(s):
  if x=='L':
   c1-=1
  elif x=='R':
   c1+=1
  elif x=='U':
   c2+=1
  else:
   c2-=1
  xp=max(xp,c1) 
  xn=min(xn,c1)
  yp=max(yp,c2)
  yn=min(yn,c2) 
 if abs(xp-xn+1)<=m and abs(yp-yn+1)<=n:
  print('safe')
 else:
  print('unsafe')
