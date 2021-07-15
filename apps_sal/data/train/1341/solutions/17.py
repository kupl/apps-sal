for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 front = [0 for i in range(n)]
 back = [n-1 for i in range(n)]
 for i in range(1,n):
  if front[i-1]==i-1 and arr[i]>arr[i-1]:
   front[i] = i
  else:
   front[i] = front[i-1]
 for i in range(n-2,-1,-1):
  if back[i+1]==i+1 and arr[i]<arr[i+1]:
   back[i] = i
  else:
   back[i] = back[i+1]
 ans = n-back[0]
 for i in range(1,n):
  if front[i-1]==i-1:
   ans+=1
   key = arr[i-1]
   low = back[i]
   high = n-1
   if arr[high]>key:
    flag = False
    while low<high:
     mid = (low+high)//2
     if arr[mid]>key:
      high = mid
     else:
      low = mid
     if low+1==high:
      if flag:
       high-=1
      flag = True
    mid = (low+high)//2
    if arr[mid]<=key:
     mid+=1
    ans += (n-mid)
 if back[0]==0:
  ans-=n
 print(ans)

