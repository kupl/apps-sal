for x in range(int(input())):
 n,d=list(map(int,input().split()))
 l=list(str(n))
 l1=[]
 y=0
 t=0
 while(True):
  m=min(l)
  pos=l.index(m)
  if(int(m)>=d):
   break
  else:
   l1.append(m)
  if(pos+1>=len(l)):
   break
  for x in range(pos+1):
   l.remove(l[0])
 t1="".join(l1)
 t1=str(t1)+str(d)*(len(str(n))-len(str(t1)))
 print(t1)
   

