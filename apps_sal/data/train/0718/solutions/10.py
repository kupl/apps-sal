t = int(input())
f = [0, 1]
for i in range(2, 100):
 f.append(f[i - 1] + f[i - 2])
 # print(f[i], ' ')
for i in range(t):
 n = int(input())
 cnt = 0
 for j in range(1, n + 1):
  for k in range(1, j + 1):
   print(f[cnt], end=' ')
   cnt += 1
  print()
