for _ in range(int(input())):
 n = int(input())
 s, p, v = list(map(int, input().split()))
 maxm = p//(s+1) * v
 
 for i in range(n-1):
  s, p, v = list(map(int, input().split()))
  prof = p//(s+1) * v
  
  if prof > maxm:
   maxm = prof
 
 print(maxm)
