def largest_smaller_than(a,N,key):
 start = 0
 end = N

 ans = -1

 while(end>=start):
  mid = (start+end)//2
  if(mid>=N or mid<0):
   break
  elif(a[mid]<key):
   ans = mid
   start = mid+1
  elif(a[mid]>=key):
   end = mid-1
 if(ans!=-1):
  return a[ans]
 else:
  return -1

T = int(input())
ans = []

for _ in range(T):
 N = int(input())

 A = []
 for i in range(N):
  x = [int(i) for i in input().split()]
  A.append(sorted(x))


 start = float('inf')
 sum = 0
 for i in range(N-1,-1,-1):
  start = largest_smaller_than(A[i],N,start)
  if(start==-1):
   sum = -1
   break
  sum += start
 ans.append(sum)

for i in ans:
 print(i)

