for tt in range(int(input())):
 n,k,l=list(map(int,input().split()))
 o=n//k
 if(k==1):
  if(n>1):
   print(-1)
  else:
   print(1)
  continue
 if(n%k>0):
  o+=1
 if(o>l):
  print(-1)
  continue
 if(n%k>0):
  o-=1
 l=[]
 for i in range(n):
  l.append(i%k+1)
 print(*l)

