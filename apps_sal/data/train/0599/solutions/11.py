for _ in range(int(input())):
 n = int(input())
 w = (*map(int, input().split()),)
 m = 0
 for i in range(n):
  if w[i] > w[m]: m = i
 count = 0
 gap = 0
 for i in range(m+1, m+n+1):
  if w[i%n] == w[m]:
   count += max(0,gap-n//2+1)
   gap = 0
  else: gap += 1
 print(count)
