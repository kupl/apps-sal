T = int(input())

while T>0:
 n = int(input())
 a = list(map(int, input().split()))
 prefix = [True for k in range(n)]
 suffix = [True for k in range(n)]
 
 for i in range(1, n):
  prefix[i] = prefix[i-1] and (a[i] > a[i-1])
 for i in range(n-2, -1, -1):
  suffix[i] = suffix[i+1] and (a[i] < a[i+1])
 
 lo = 0
 hi = n - 1
 while lo < hi:
  mid = (lo + hi)//2
  if suffix[mid]:
   hi = mid
  else:
   lo = mid + 1 
 ans = n - lo 
 #print(ans)
 for i in range(n-1):
  if prefix[i]:
   lo = i + 1
   hi = n - 1
   while lo < hi:
    mid = (lo + hi)//2
    if suffix[mid] and a[mid] > a[i]:
     hi = mid
    else:
     lo = mid + 1
   ans += (n - lo + 1)
   if lo == i + 1 or (lo == n-1 and a[lo] < a[i]):
    ans -=1
   #print(ans)
  else:
   break
 if prefix[-1]:
  ans -= 1
 print(ans)
 T-=1
 
  

