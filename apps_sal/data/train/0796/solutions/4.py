tc = int(input())
for _ in range(tc):
 n = int(input())
 arr = list(map(int, input().split()))
 st = 0
 en = st + 1
 res = []
 while st < n:
  while True:
   if en == n:
    break
   if arr[en-1] > 0 and arr[en] < 0:
    en += 1
    continue
   if arr[en-1] < 0 and arr[en] > 0:
    en += 1
    continue
   break
  for i in range(st, en):
   res.append(en - i)
  st = en
  en = en + 1
 print(' '.join(map(str, res)))

