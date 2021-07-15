t = int(input())
while t > 0:
 n = int(input())
 li = [int(x) for x in input().split()]
 li.sort(reverse=True)
 c = 0
 for i in range(n):
  if i % 2 == 0:
   c += li[i]
 print(c)
 t = t - 1

