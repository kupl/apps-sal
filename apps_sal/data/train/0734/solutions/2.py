for q in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 d=[]
 for i in range(len(l)):
  d.append((l[i],i))
 l.sort()
 d.sort()
 i=0
 count=[]
 while i<n:
  x=l[i]
  j=0
  c=0
  while i+j<n and l[i+j]==x:
   c+=1
   j+=1
  count.append(c)
  i+=j
 c=max(count)
 if c>n//2:
  print('No')
 else:
  ans=[0]*n
  for i in range(len(l)):
   ans[d[i][1]]=d[i-c][0]
  print('Yes')
  print(*ans)

