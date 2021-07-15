for _ in range(int(input())):
 N = int(input())
 a = list(map(int, input().split()))
 b = a[::-1]
 maxx = 0
 dic = {}
 for index, items in enumerate(b):
  k = 0
  if items not in list(dic.keys()):
   for i in range(N - index):
    if a[i] % items == 0:
     k += 1
     dic[a[i]] = 0
  maxx = max(k-1, maxx)
 print(maxx)

