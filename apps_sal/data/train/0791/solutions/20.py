import sys

t = int(sys.stdin.readline().strip())

while t:

 n, d = list(map(int, sys.stdin.readline().strip().split(" ")))
 nums = list(map(int, sys.stdin.readline().strip().split(" ")))
 a = False
 s = 0
 for i in nums:
  s = s + i
 avg = s//n
 ans = 0
 count = 0
 if s%n != 0:
  ans = -1
 else:
  arr = [avg]*n
  
  for i in range(len(arr)-d):
   k = arr[i] - nums[i]
   if k!=0:
    arr[i] = arr[i] - k
    arr[i+d] = arr[i+d] + k
    count += abs(k)
  for i in range(len(arr)):
   if arr[i] != nums[i]:
    ans = -1
    a = True
    break

  if a != True:
   ans = count
 print(ans)
 t-=1

