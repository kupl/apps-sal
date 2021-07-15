t=int(input())
while t:
 n = int(input())
 arr = [int(x) for x in input().split()]
 cnt = 1
 min_sp = arr[0]
 for i in range(1,n):
  if(min_sp>arr[i]):
   min_sp = min(min_sp,arr[i])
   cnt = cnt + 1
 print(cnt)
 t=t-1
