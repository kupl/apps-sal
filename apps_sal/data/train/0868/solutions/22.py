import math
import heapq
def counting_sort(array1, max_val):
 m = max_val + 1
 count = [0] * m
 for a in array1:
  count[a] += 1
 i = 0
 for a in range(m):
  for c in range(count[a]):
   array1[i] = a
   i += 1
 return array1
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 l=list(map(int,input().split()))
 M=[]
 ans=0
 for i in range(n):
  for j in range(i,n):
   m=math.ceil(k/(j-i+1))
   gt=(k-1)//m
   M.append(gt)
  break
 for i in range(n):
  max=-1
  s=set()
  d={}
  hallo_frnd={}
  for j in range(i,n):
   x=None
   value=M[j-i]
   if l[j] not in d:
    d[l[j]]=1
   else:
    d[l[j]]+=1
   if l[j]>max:
    max=l[j]
   if value not in s:
    ####
    s.add(value)
    x=max
    hallo_frnd[value]=max
   else:
    if l[j]<hallo_frnd[value]:
     yt=l[i:j+1]
     heapq.heapify(yt)
     x=heapq.nsmallest(value+1,yt)[-1]
     hallo_frnd[value]=x
    else:
     x=hallo_frnd[value]
   if d[x] in d:
    ans+=1
 print(ans)

