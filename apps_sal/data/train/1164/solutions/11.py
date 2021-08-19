from collections import defaultdict
from operator import itemgetter
(p, s) = map(int, input().split())
diff = []
for _ in range(p):
    sc = list(map(int, input().split()))
    nk = list(map(int, input().split()))
    arr = zip(sc, nk)
    arr_sort = sorted(arr, key=itemgetter(0))
    temp = 0
    for i in range(s - 1):
        if arr_sort[i][1] > arr_sort[i + 1][1]:
            temp += 1
    a = [temp, _ + 1]
    diff.append(a)
'\ntemp = diff[:]\n\n# temp = [(1, 2),(1, 1),(2, 1),(2, 3)]\ntemp.sort(key=lambda x: (x[0], x[1]))\n\n# print(temp)\n\nt = 1\nd = defaultdict(int)\nfor i in temp:\n    d[i] = t\n    t += 1\n\nfor i in diff:\n    print(d[i])\n'
v1 = sorted(diff, key=itemgetter(0))
for i in v1:
    print(i[1])
