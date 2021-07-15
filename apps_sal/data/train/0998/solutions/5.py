for u in range(1):
 n,q=list(map(int,input().split()))
 l,d=[0]*n,[0]*n
 for i in range(q):
  s=input().split()
  if(s[0]=='RowAdd'):
   x,y=int(s[1]),int(s[2])
   l[x-1]+=y
  else:
   x,y=int(s[1]),int(s[2])
   d[x-1]+=y
 print(max(l)+max(d))

