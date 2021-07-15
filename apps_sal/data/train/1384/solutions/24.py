def solve(arr,n,k):
 lbs = 0
 for i in range(0,n-k+1):
  cnt = k
  for j in range(i-1,-1,-1):
   if(arr[j]==1):
    cnt+=1
   else:
    break
  for j in range(i+k,n):
   if(arr[j]==1):
    cnt+=1
   else:
    break 
  lbs = max(lbs,cnt)
 return lbs

t = int(input())
while t>0:
 t-=1
 n,k = map(int,input().split())
 arr = list(map(int,list(input().strip())))
 print(solve(arr,n,k))
