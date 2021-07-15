for _ in range(int(input())):
 sg = input().strip()
 l = len(sg)
 if l % 2 != 0:
  print(-1)
 else:
  ones = 0; zeros = 0;
  for i in range(l):
   if sg[i] == '1':
    ones += 1
   else:
    zeros += 1
  diff = abs(ones - zeros)
  if diff == l:
   print(-1)
  else:
   diff //= 2
   print(diff)

