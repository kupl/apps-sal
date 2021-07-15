def check(n, a, b):
 for i in range(1, n): 
  if a[i] == 0: return False
 for i in range(n-1): 
  if b[i] == 0: return False
 if a[-1] != b[0] or a[0] != 0 or b[-1] != 0: return False
 else:
  d = b[0]
  for i in range(1, n-1):
   if d > a[i] + b[i]: return False
  for i in range(1, n-1):
   if a[i] > d + b[i]: return False
   if b[i] > d + a[i]: return False
 return True

for _ in range(int(input())):
 n = int(input())
 a = [int(i) for i in input().split()]
 b = [int(i) for i in input().split()]

 if check(n, a, b): print('Yes')
 else: print('No')
