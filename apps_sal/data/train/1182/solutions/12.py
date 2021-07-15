n =[]
for i in range(int(input())):
 n.append(int(input()))
for m in n:
 r=[]
 c=0
 for a in range(m+1, 2*m+1):
  b = (a*m)//(a-m)
  if (a*b%m==0):
   c+=1
   r.append(a)
 print(c)
 for a in r:
  print(a)
