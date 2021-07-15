# cook your dish here
for _ in range(int(input())):
 n,k=map(int,input().split())
 l=list(map(int,input().split()))
 m=[]
 t=[]
 ms=ts=0
 for i in range(n):
  if (i%2)==0:
   m.append(l[i])
  else:
   t.append(l[i])
 ms=sum(m)
 ts=sum(t)
 if ts>ms:
  print('YES')
 else:
  flag=1
  while k>0:
   mm=max(m)
   mn=min(t)
   ts=ts+mm-mn
   ms=ms-mm+mn
   if ts>ms:
    flag=0
    print('YES')
    break
   k-=1
  if flag==1:
   print('NO')
