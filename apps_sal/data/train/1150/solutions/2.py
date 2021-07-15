for _ in range(int(input())):
  n = int(input())
  count = 0
  while n>0:
   r = int(n ** 0.5)
   n = n - r*r
   count+=1
  print(count)
