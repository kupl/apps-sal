# cook your dish here
for i in range(int(input())):
 n,m,s=map(int,input().split(" "))
 h1,t,count = list(map(int,input().split( ))),[],0
 t=[x for x in h1 if x<=2*s]
 if len(t)==0:print(0)
 else:
  count=sum(map(lambda x: x<=s,t))
  if count>=m:print(m) 
  elif m>=count+(len(t)-count)*2:print(len(t)) 
  else:print(count+(m-count)//2)
