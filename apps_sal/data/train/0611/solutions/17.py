t=int(input())
while t>0:
 n=int(input())
 a=list(map(int,input().split(' ')))
 d={}
 k={}
 for i in a:
  k[i]=1
 flag=0
 for i in range(len(a)):
  if d.get(a[i],0)==0:
   d[a[i]]=[i+1]
  else:
   d[a[i]].append(i+1)
 
 for i in list(d.keys()):
  c=0
  for j in d[i]:
   if k.get(j,0)==1:
    c+=1
  if c>=2:
   flag=1
   break
 if flag==1:
  print('Truly Happy')
 else:
  print('Poor Chef')
 t-=1

