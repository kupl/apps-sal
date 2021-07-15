tmp=input().split(' ',2)
m=int(tmp[0])
n=int(tmp[1])
lis=[0]*m

for k in range(n):
 s=input()
 if s=='CLOSEALL':
  for o in range(m):
   lis[o]=0
 else:
  s=s.replace('CLICK ','')
  s=int(s)
  if lis[s-1]==1:
   lis[s-1]=0
  else:
   lis[s-1]=1
 
 sum=0
 for u in range(m):
  sum+=lis[u]
 print(sum) 
