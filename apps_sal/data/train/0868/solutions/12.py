import heapq

t=int(input())
for y in range(t):
 (n, k )=(int(x) for x in input().split())
 places=[]
 for l in range(1,n+1):
  m=(k-1)//l+1
  shoot=m*l-k
  place=shoot//m+1
  places.append(place)
 A=[int(x) for x in input().split()]
 heaps=[[-x] for x in A]
 assert(len(A)==n)
 ans=A.count(1)
 for l in range(1,n):
  elements=[0]*2001
  for e in A[:l+1]:
   try:
    elements[e]+=1
   except:
    elements[e]=1
  for s in range(0,n-l):
   heapq.heappush(heaps[s],-A[s+l]) 
   if places[l]>2:
    reserve=[]
    for i in range(places[l]):
     reserve.append(heapq.heappop( heaps[s]))
    for r in reserve:
     heapq.heappush(heaps[s],r)
    x=-reserve[-1]
   elif (places[l]==2):
    x=max(-heaps[s][1],heaps[s][2])
   else:
    x=-heaps[s][0]
   f=elements[x]
   try:
    if elements[f]>0:
     ans+=1
   except:
    pass
   if s<n-l-1:
    try:
     elements[A[s]]-=1
     elements[A[s+l+1]]+=1
    except: 
     elements[A[s+l+1]]=1
 print(ans)
