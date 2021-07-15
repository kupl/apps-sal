import sys

def __starting_point():
 n,k = [int(u) for u in sys.stdin.readline().strip().split()]
 val = [int(u) for u in sys.stdin.readline().strip().split()]
 ans = ""
 if k > 0:
  maxval = max(val)
  for i in range(n):
   val[i] = maxval - val[i]
  maxval = max(val)
  if k%2 == 0:
   for i in range(n):
    ans += str(maxval - val[i]) + ' '
   print(ans[:-1])
  else:
   for i in range(n):
    ans += str(val[i]) + ' '
   print(ans[:-1])
 else:
  for i in range(n):
   ans += str(val[i]) + ' '
  print(ans[:-1])

__starting_point()
