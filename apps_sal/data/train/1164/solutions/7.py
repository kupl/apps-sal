from collections import defaultdict
from operator import itemgetter

p, s = list(map(int, input().split()))

diff = []
for _ in range(p):
 sc = list(map(int, input().split()))
 nk = list(map(int, input().split()))

 arr = list(zip(sc, nk))

 arr_sort = sorted(arr, key = itemgetter(0))
 # print(arr)
 temp = 0
 for i in range(s-1):
  if arr_sort[i][1] > arr_sort[i+1][1]:
   temp += 1
 a = (temp, _+1)
 diff.append(a)

temp = diff[:]
temp.sort(key=lambda x: x[0])


for i in temp:
 print(i[1])

