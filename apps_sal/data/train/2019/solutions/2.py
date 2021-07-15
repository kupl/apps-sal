from math import ceil
n = int (input())
a = list (map (int, input().split()))
m = max (max (a), ceil(sum(a)/(n-1)))
acc = 0
for i in a:
  acc += m - i
if acc >= m:
  print (m)
else:
  print(m + ceil((m-acc)/n))

