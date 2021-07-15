for _ in range(int(input())):
 N, K = map(int, input().split())
 array = list(map(int, input().split()))
 count = 0
 mn = float('inf')
 for i in range(N):
  for j in range(i+1,N):
   if abs(array[i] + array[j] - K) < mn:
    mn = abs(array[i] + array[j] - K)
    count = 1
   elif abs(array[i] + array[j] - K) == mn:
    count+=1
 print(mn, count)
