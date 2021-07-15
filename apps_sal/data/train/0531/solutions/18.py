import numpy as np
n = int(input())
arr = np.empty((n,2),dtype=int)
for i in range(n):
 x = list(map(int,input().split()))
 arr[i]=x
flag = 'l'
if(n==1):
 ans=1
else:
 ans=2
for i in range(1,n-1):
 curr = arr[i]
 pre = arr[i-1]
 next = arr[i+1]
 if(flag=='l'):
  cn_l = curr[0]-curr[1]
  cn_r = curr[0]+curr[1]
  if(cn_l>pre[0]):
   flag='l'
   ans+=1
  elif(cn_r<next[0]):
   flag='r'
   ans+=1
 elif(flag=='r'):
  cn_l = curr[0] - curr[1]
  cn_r = curr[0] + curr[1]
  pre_r = pre[0] + pre[1]
  if(cn_l > pre_r):
   flag = 'l'
   ans+=1
  elif(cn_r < next[0]):
   flag='r'
   ans+=1
print(ans)

