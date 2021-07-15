T = int(input())
for i in range(T):
 n = int(input())
 k = int(input())
 r = k % n
 if r == n-r:
  print(n-1)
 else:
  print(2*min(r, n-r))

