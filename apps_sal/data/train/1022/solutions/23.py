t = int(input())
while t:
 t -= 1
 n = int(input())
 a = list(map(int, input().strip().split()))
 if n % 2:
  print("NO")
 else:
  okay = True
  p = n // 2
  for i in range(p):
   if a[i] == -1 and a[i + p] == -1:
    a[i] = a[i + p] = 1
   elif a[i] == -1:
    a[i] = a[i + p]
   elif a[i + p] == -1:
    a[i + p] = a[i]
   elif a[i] != a[i + p]:
    okay = False
  if okay:
   print("YES")
   for x in a:
    print(x, end = " ")
   print()
  else:
   print("NO")


