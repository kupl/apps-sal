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
 a = [temp, _+1]
 diff.append(a)
temp = diff[:]

# temp = [(1, 2),(1, 1),(2, 1),(2, 3)]
temp.sort(key=lambda x: (x[0], x[1]))

# print(temp)
'''
t = 1
d = defaultdict
for i in temp:
    d[i] = t
    t += 1
'''
diff = sorted(diff, key = lambda x: x[0])

for i in diff:
 print(i[1])
'''
v1=sorted(diff,key = itemgetter(0))
for i in v1:
    print(i[1])
    '''

