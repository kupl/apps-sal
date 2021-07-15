t = int(input())
while t>0:
 t -= 1
 n = int(input())
 a = [int(x) for x in input().split()]
 m = max(a)
 ind = []
 for i in range(n):
  if a[i] == m:
   ind.append(i)
 if len(ind) == 1:
  print(n//2)
  continue
 f = ind[0]
 l = ind[-1]
 width = l-f+1
 if width > n//2:
  print(0)
 else:
  print(n//2-width+1)









