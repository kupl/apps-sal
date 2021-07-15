import bisect

for _ in range(int(input())):
 n, q = list(map(int, input().split()))
 ar = list(map(int, input().split()))

 new = ar.copy()
 new.sort()

 for __ in range(q):
  x, y = list(map(int, input().split()))
  cost = abs(ar[y - 1] - ar[x - 1]) + y - x

  length = bisect.bisect_right(new, max(ar[y - 1], ar[x - 1]))
  length -= bisect.bisect_left(new, min(ar[x - 1], ar[y - 1]))

  print(cost, length)

