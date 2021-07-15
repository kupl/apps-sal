while True:
 n = int(input())
 if n==0:
  break
 else:
  ambiguous = 1
  a =[int(k) for k in input().split()]
  for i in range(0, n):
   if a[i]- 1 >= n or a[i] < 1 or a[a[i] - 1] != i + 1:
    print('not ambiguous')
    ambiguous = 0
    break
  if ambiguous == 1:
   print('ambiguous')
