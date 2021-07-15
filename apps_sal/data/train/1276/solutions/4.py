t = eval(input())
for tt in range(t):
 nk = input().split()
 n = int(nk[0])
 k = int(nk[1])
 lis = input().split()
 for i in range(n):
  lis[i] = int(lis[i])
 tmp = []
 for i in range(k):
  tmp.append(1 << i)
 count = 0
 for i in tmp:
  if i not in lis:
   count += 1
 print(count)
