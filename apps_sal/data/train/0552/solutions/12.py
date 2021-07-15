for _ in range(int(input())):
 n,k = list(map(int, input().split()))
 weight = list(map(int, input().split()))
 weight.sort()
 a, b = 0, 0
 for i in range(n):
  if i < k:
   a += weight[i] 
   
  if i >= n-k:
   b += weight[i] 
 
 print(max(abs(a-(sum(weight) - a)), abs(b-(sum(weight)-b))))

