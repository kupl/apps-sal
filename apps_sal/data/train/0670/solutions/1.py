for i in range(int(input())):
 n = int(input())
 a = sorted([int(i) for i in input().split()])
 m = False
 d = []
 for i in range(1, n):
  if a[i] - a[i - 1] != 0:
   d.append(a[i] - a[i - 1])
  if a[i] - a[i - 1] != 0 and a[0] % (a[i] - a[i - 1]) != 0:
   m = True
   break
 if m:
  print(n)
 else:
  if not d:
   print(a[0] * n)
  else:
   d = sorted(d)
   print(n * d[0])
