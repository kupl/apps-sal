import sys, bisect

t = int(input())

for _ in range(t):

 n, k, m = list(map(int, input().split()))
 p = list(map(int, input().split()))
 c = list(map(int, input().split()))
 w = list(map(int, input().split()))
 b = list(map(int, input().split()))
 w.sort()
 b.sort()

 uncomp = 0

 for x in range(n):
  diff = p[x] - c[x]
  i = bisect.bisect_right(w, diff)
  j = bisect.bisect_right(b, diff)
  if i: w0 = w[i-1]
  else: w0 = -1
  if j: b0 = b[j-1]
  else: b0 = -1
  if w0 > b0 and w0 != -1:
   p[x] -= w0
   del w[i-1]
  elif b0 != -1:
   c[x] += b0
   del b[j-1]
  uncomp += p[x] - c[x]

 print(uncomp)
