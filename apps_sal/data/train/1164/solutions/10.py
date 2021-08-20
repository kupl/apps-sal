from collections import defaultdict
from operator import itemgetter
(p, s) = list(map(int, input().split()))
diff = []
for _ in range(p):
    sc = list(map(int, input().split()))
    nk = list(map(int, input().split()))
    arr = list(zip(sc, nk))
    arr_sort = sorted(arr, key=itemgetter(0))
    temp = 0
    for i in range(s - 1):
        if arr_sort[i][1] > arr_sort[i + 1][1]:
            temp += 1
    a = [temp, _ + 1]
    diff.append(a)
temp = diff[:]
temp.sort(key=lambda x: (x[0], x[1]))
'\nt = 1\nd = defaultdict\nfor i in temp:\n    d[i] = t\n    t += 1\n'
diff = sorted(diff, key=lambda x: x[0])
for i in diff:
    print(i[1])
'\nv1=sorted(diff,key = itemgetter(0))\nfor i in v1:\n    print(i[1])\n    '
