
#island=[[0 for i in range(k+2)]for j in range(n)
for _ in range(int(input())):
 island=[]
 n,k=map(int,input().split())
 for i in range(n):
  l=[int(i) for i in input().split()]
  l=l[1:]
  island.append(l)
 cnt=[0]*(k+1)
 for i in range(n):
  for indigrient in island[i]:
   cnt[indigrient]+=1 
 f=1 
 for i in range(1,k+1):
  if cnt[i]==0:
   f=0 
   break 
 if not f:
  print('sad')
  continue 
 f1=0 
 # print(island)
 for i in range(n):
  f2=1 
  for j in island[i]:
   if cnt[j]==1:
    f2=0
  if f2:
   f1=1 
   break 
 if f1:
  print('some')
 else:
  print('all')
