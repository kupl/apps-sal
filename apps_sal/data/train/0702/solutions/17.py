# cook your dish here
t=int(input())
for i in range(t):
 inp=input()
 m,tc,th=inp.split()
 m=int(m)
 tc=int(tc)
 th=int(th)
 diff=th-tc
 if(diff==0):
  print("No")
 if(diff>0):
  if(diff%3==0 and (diff/3)<=m):
   print("No")
  else:
   print("Yes")

