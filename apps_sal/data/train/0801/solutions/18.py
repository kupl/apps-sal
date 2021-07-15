for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 b = list(map(int, input().split()))
 minimum = min(min(a), min(b))
 s = set()
 ad = {}
 bd = {}
 for i in a:
  if i in s:
   s.remove(i)
  else:
   s.add(i)
  ad[i] = ad.setdefault(i, 0) + 1
  bd[i] = bd.setdefault(i, 0) - 1
 for i in b:
  if i in s:
   s.remove(i)
  else:
   s.add(i)
  bd[i] = bd.setdefault(i, 0) + 1
  ad[i] = ad.setdefault(i, 0) - 1
 if len(s) > 0:
  print("-1")
  continue
 a = []
 b = []
 for i in ad.keys():
  if ad[i] > 0:
   a.extend([i] * (ad[i] // 2))
 for i in bd.keys():
  if bd[i] > 0:
   b.extend([i] * (bd[i] // 2))
 cost = 0
 for i in range(len(a)):
  cost += min(min(a[i], b[len(a) - 1 - i]), 2 * minimum)
 print(cost)
