n=int(input())
hit=list(map(int,input().split()))

d={}
for i in range(1,n):
 x1,x2=hit[i],hit[i-1]
 try: d[x1^x2]+=[i]
 except: d[x1^x2]=[i]

done=False
for i in d:
 x=d[i]
 if len(x)>2: done=True; break
 elif len(x)==2:
  x=sorted(x)
  if x[0]!=x[1]-1: done=True; break

if done: print('Yes')
else:
 v={}
 for i in hit:
  try: v[i]+=1
  except: v[i]=1
 x={}
 h=list(v.values())
 for i in h:
  try: x[i]+=1
  except: x[i]=1
 if ( 2 in x and x[2]==2 ) or ( 4 in x and x[4]==1 ): print('Yes')
 else: print('No')

