def left_span(arr,n):
 ans=[0]
 span=[0]
 for i in range(1,n):
  
  while span and arr[i]>arr[span[-1]]:
   span.pop()
  
  if not span:
   ans.append(0)
   
  else:
   ans.append(span[-1]+1)
  span.append(i)
 return ans

def right_span(arr,n):
 ans=[n+1]
 span=[n-1]
 for i in range(n-2,-1,-1):
  
  while span and arr[i]>=arr[span[-1]]:
   span.pop()
   
  if not span:
   ans.append(n+1)
  else:
   ans.append(span[-1]+1)
  span.append(i)
 return ans[::-1]
from collections import Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
n,q=list(map(int,input().split( )))
arr=list(map(int,input().split( )))

left=left_span(arr,n)
right=right_span(arr,n)
c=Counter()
for i in range(n):
 c[arr[i]]+=(right[i]-(i+1))*(i+1-left[i])
a=sorted(c)
f=[]
for v in a:
 f.append(c[v])
prefix_sum=[f[0]]
n=len(f)
for i in range(1,n):
 prefix_sum.append(f[i]+prefix_sum[-1])
r=[0]*q
for i in range(q):
 sign,k,player=list(map(str,input().split( )))
 k=int(k)
 if sign=="=":
  if k in c:
   res=c[k]
  else:
   res=0
 elif sign==">":
  j=bisect_left(a,k)
  if j==n:
   res=0
  elif a[j]==k:
   res=prefix_sum[-1] - prefix_sum[j]
  else:
   if j>0:
    res=prefix_sum[-1] - prefix_sum[j-1]
   else:
    res=prefix_sum[-1]
 else:
  j=bisect_left(a,k)
  if j==0:
   res=0
  else:
   res=prefix_sum[j-1]
 
 if res%2==0:
  if player=="D":
   r[i]="C"
  else:
   r[i]="D"
 else:
  r[i]=player
print(''.join(r))
   
  



