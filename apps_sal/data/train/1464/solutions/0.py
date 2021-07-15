t=int(input())
li1=[31,29,31,30,31,30,31,31,30,31,30,31]
li2=[31,28,31,30,31,30,31,31,30,31,30,31]
for z in range(t):
 y,m,d=list(map(int,input().split(':')))
 if y%4 == 0:
  if y%100 == 0:
   if y%400 == 0:
    li=li1
   else:
    li=li2
  else:
   li=li1
 else:
  li=li2
 c=0
 if d%2 == 0:
  while d%2 == 0:
   c+=1
   d+=2
   if d>li[m-1]:
    d=d%li[m-1]
    m+=1
 else: 
  while d%2 != 0:
   c+=1
   d+=2
   if d>li[m-1]:
    d=d%li[m-1]
    m+=1
 print(c)
   

