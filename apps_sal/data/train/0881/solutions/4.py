t = int(input())
for i in range(t):
 N = int(input())
 st = input().split()
 L = []
 for x in st:
  L.append(int(x))
 n = 1
 cnt = 1
 for p in range(1,N):
  if L[p] < L[p-1]:
   n += 1
   cnt = 1
  else:
   cnt += 1
   n += cnt
  p += 1
 print(n)


