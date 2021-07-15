T=int(input())
for i in range(0,T):
 t=[]
 count=0
 n,m,s=list(map(int,input().split(" ")))
 h=list(map(int,input().split( )))
 h1=list(h)
 
 t=[x for x in h1 if x<=2*s]
 if len(t)==0:
  print(0)
 else:
  count=sum([x<=s for x in t])
  if count>=m:
   print(m)
  
  elif m>=count+(len(t)-count)*2:
   print(len(t))
   
  else:
   print(count+(m-count)//2)


