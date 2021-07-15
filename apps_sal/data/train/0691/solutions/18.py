for _ in range(int(input())):
 N = int(input())
 a = list(map(int, input().split()))
 b = a[::-1]
 maxx = 0
 dic = {}
 for index, items in enumerate(b):
  k = 0
  try:
   if dic[items]==0:
    pass
  except Exception as e:
   for i in range(N - index):
    if a[i] % items == 0:
     k += 1
     dic[a[i]] = 0
  maxx = max(k-1, maxx)
 print(maxx)

