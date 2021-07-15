T=int(input())
for xs in range(T):
 N,Q=[int(o) for o in input().split()]
 a=[int(o) for o in input().split()]
 b=sorted(a)
 Di={} #Dictionary
 for i in range(len(a)):
  Di[a[i]]=[i]
 for i in range(len(b)):
  Di[b[i]].append(i) 
 r=[]
 qu=[int(input()) for j in range(Q)]
 for q in qu:
  low=1
  high=N
  ind=Di[q][0]+1
  b=[]
  f=[]
  s=0
  maxs=N-Di[q][1]-1
  mins=N-maxs-1
  while low<=high:   #Binary Search algorithm
   mid=(low+high)//2
   if mid==ind:
    break
   elif mid<ind:
    low=mid+1
    if a[mid-1]>q:
     b.append(a[mid-1])
    else:
     mins-=1 
   elif mid>ind:
    high=mid-1
    if a[mid-1]<q:
     f.append(a[mid-1])
    else:
     maxs-=1
  lenf=len(f)
  lenb=len(b)
  sw=min(lenf,lenb)
  rs=max(lenf,lenb)-sw
  mins,maxs=mins-sw,maxs-sw
  ex=min(mins,maxs)
  if ex<rs: 
   r.append(-1)
   s=1
  else:
   sw+=rs # When ex>=rs
  if not s:
   r.append(sw) 
 for ans in r:
  print(ans) #Final
