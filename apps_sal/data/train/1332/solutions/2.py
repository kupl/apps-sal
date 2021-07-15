n = int(input())
for t in range(n):
 (a,b) = [int(x) for x in input().split()]
 count = 0
 while(not a == b):
  if (a>b):
   a = a/2
  else:
   b = b/2
  count += 1
 print(count)

