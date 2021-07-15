t=int(input())
m=[int(input()) for i in range(t)]
for i in m:
 c=0
 ANS=[]
 for a in range(i+1,2*i+1,1):
  intp=a*i/(a-i)
  if intp>=a and a*i%(a-i)==0:
   c=c+1
   ANS.append(a)
 print(c)
 for j in ANS:
  print(j)

