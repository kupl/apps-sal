n,m,p=list(map(int,input().split()))
mn={}
for i in range (0,p):
 x,y=list(map(int,input().split()))
 key = (x,y)
 if key in mn:
  mn[key] +=1
 else:
  mn[key] = 1


#print mn
ans = {}
for key in (mn):
 cur = key 
 next = (key[0],key[1]+1)
 if next[1] <= m:
  if next in mn:
   if mn[cur] > mn[next]+1:   # Strictly correct.
    ans[cur[0]] = -1
  elif mn[cur] > 1:
   ans[cur[0]] = -1
  
for i in range(1,n+1):
 if i in ans:
  print(-1)
 else:
  start = (i,1)
  end = (i,m)
  #if start != end:
  if end in mn and start in mn:
   print(mn[end]-mn[start]+(m-1))
  if end in mn and start not in mn:
   print(mn[end]+(m-1))
  if end not in mn and start in mn:
   print((m-1)-mn[start])
  if end not in mn and start not in mn:
   print(m-1)
  #else:
   #print mn[start]+1

