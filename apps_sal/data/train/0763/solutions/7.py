# cook your dish here
t = int(input())

for _ in range(t):
 n = int(input())
 s = input()
 p = input()
 
 o=0
 z=0
 o2=0
 z2=0
 for i in s:
  if(i=='1'):
   o+=1
  else:
   z+=1
 
 flag=0
 
 for i in p:
  if(i=='1'):
   o2+=1
  else:
   z2+=1
 
 spareone=0
 if(o==o2 and z == z2):
  for i in range(n):
   if(s[i]!=p[i]):
    if(p[i]=='0'):
     spareone+=1
    if(p[i]=='1'):
     if(spareone==0):
      flag=1
      break
     else:
      spareone=spareone-1
  
  if(flag==0):
   print("Yes")
  else:
   print("No")
 else:
  print("No")

