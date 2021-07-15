T = int(input())

for t in range(T):
 
 n, k = map(int, input().split())
 
 arr = list(map(int, input().split()))
  
 out1 = set(arr)
 
 minSum = sum(arr[0:k])
 
 for i in range(1, n-k+1):
  
  temp = arr[i:i+k]
  
  out = set(temp)
  
  if(len(out) == len(out1)):
   currentSum = sum(temp)
   if minSum < currentSum:
    minSum = currentSum
 print(minSum)
