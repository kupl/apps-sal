# cook your dish here
onehour=30 
oneminute=0.5 
d={0:0,5:30,10:60,15:90,20:120,25:150,30:180,35:210,40:240,45:270,50:300,55:330}
t=int(input())
for _ in range(t):
 h,s=list(map(int,input().split(":")))
 h=h%12 
 initial=h*5 
 modu=s%5 
 s+=modu 
 deg=d[s]-d[initial]
 
 if deg>=0:
  deg=deg-s*0.5
 else:
  deg=abs(deg)+s*0.5
 if deg>180:
  deg=360-deg 
 if deg==int(deg):
  print(abs(int(deg)),"degree")
 else:
  print(abs(deg),"degree")

