import operator
n, m, p = list(map(int, input().split()))
a = []
for i in range(p):
 a.append(list(map(int, input().split())))
a.sort(key=operator.itemgetter(0, 1))
b = []
j = p - 1
for i in range(n, 0, -1):
 last = 200000
 now = 0
 k = m
 low = 1
 high = m
 while j >= 0 and a[j][0] == i:
  if a[j][1] == k:
   now += 1
   if now > last + 1:
    break
  elif a[j][1] == k - 1:
   k = a[j][1]
   last = now
   now = 1
  else:
   k = a[j][1]
   now = 1
   last = 0
  if a[j][1] == m:
   high = now + a[j][1]
  if a[j][1] == 1:
   low = now + a[j][1]
  j -= 1
 if now > last + 1:
  b.append(-1)
  while j >= 0 and a[j][0] == i:
   j -= 1
 else:
  b.append(high - low)
for i in range(n - 1, -1, -1):
 print(b[i])

