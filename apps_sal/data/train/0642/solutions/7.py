for _ in range(int(input())):
 n,d=map(int,input().split())
 c=list(map(int,input().split()))
 c.sort()
 left=0
 right=10**10
 pos=0
 while left<=right:
  con=0
  mid=(left+right)//2
  nxt=c[0]+mid
  for i in range(1,n):
   if nxt<c[i]:
    nxt=c[i]+mid
   elif nxt>=c[i] and nxt<=c[i]+d:
    nxt+=mid
   else:
    con=1
    break
  if con!=1:
   pos=mid
   left=mid+1
  else:
   right=mid-1
 left=0
 right=999999
 pos1=0
 #print(pos)
 while left<=right:
  con=0
  mid=(left+right)//2
  l=len(str(mid))
  b=['0']*(6-l)
  b+=[str(mid)]
  b=''.join(b)
  nxt1=str(pos)+'.'+b
  nxt1=float(nxt1)
  nxt=c[0]+nxt1
  for i in range(1,n):
   if nxt<c[i]:
    nxt=c[i]+nxt1
   elif nxt>=c[i] and nxt<=c[i]+d:
    nxt+=nxt1
   else:
    con=1
    break
  if con!=1:
   pos1=nxt1
   left=mid+1
  else:
   right=mid-1
 print(format(pos1,'.6f'))
