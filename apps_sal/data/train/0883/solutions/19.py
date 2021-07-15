t= int(input())
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 jhol=0
 d={}
 for i in a:
  if( i in d):
   d[i]+=1
  else:
   d[i]=1
 if(len(d)>2):
  jhol=1
  print(-1)
 elif(len(d)==1):
  b=list(set(a))
  x=b[0]
  if(d[x]==n and x==(n-1)):
   print(0)
  elif(x==0):
   print(n)
  else:
   print(-1)
 else:
  b=set(a)
  x=d[max(b)]
  y=max(b)
  if(y==d[min(b)]):
   print(x)
  else:
   print(-1)
