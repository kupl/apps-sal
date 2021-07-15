T = int(input())
for j in range(1, T+1):
 N, B = input().split()
 N = int(N)
 B = int(B)
 k = N
 fs = 0
 maxim = 0
 for i in range(1, N+1):
  N = k
  fs = 0
  ss = 0
  fs = fs + i
  N = N-i
  while (N>=B):
   ss = ss + fs
   N = N-B
  if ss > maxim:
   maxim = ss
 print(maxim)
  
  

