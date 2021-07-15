for T in range(0, int(input())):

 n, z1, z2 = map(int, input().split())

 x = list(map(int, input().split()))
 y = x

 for i in range(0, n):
  y.append(-x[i])

 res = 0

 for i in range(0, n):
  if (abs(x[i]) == abs(z1) or abs(x[i]) == abs(z2)):
   res = 1
   break

 if res == 0:
  for i in range(0, 2*n):
   flag = 0
   for j in range(0, 2*n):
    if y[i] + y[j] == z1 or y[i] + y[j] == z2:
     flag = 1
     break

   if flag == 0:
    break
  if flag == 1:
   res = 2


 print(res)
