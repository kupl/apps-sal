def isValid(arr,mid,n):
 t = 0.0
 for i in range(n):
  if t<arr[i]:
   t = arr[i] + mid
  elif t<=arr[i] + d:
   t = t + mid
  else:
   return False
 return True


for _ in range(int(input())):
 n,d = list(map(int,input().split(' ')))
 arr = [int(num) for num in input().split(' ')]
 duration = []
 ans = -1
 arr.sort()
  
 left = 0.0
 right = 10000000000
 while right -left >= 10**(-6):
  mid = (left+right)/2
  #print(mid)
  if isValid(arr,mid,n)==True:
   left = mid
   ans = mid
  else:
   right = mid
   
 print(ans)

