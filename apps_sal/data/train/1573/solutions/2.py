T = int(input())
for _ in range(T):
 n = int(input())
 if n%2 == 0:
  print("NO")
 else:
  print("YES")
  count = 0
  for _ in range(n):
   count += 1
   d = [0 for _ in range(n)]
   z = int((n - 1)/2)
   for i in range(z):
    if count + i< n-1:
     d[count + i] = 1
    else:
     d[count + i - n] = 1
   for i in d:
    print(i, end="")
   print()
