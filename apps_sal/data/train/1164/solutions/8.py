from collections import defaultdict
from operator import itemgetter
(p, s) = map(int, input().split())
diff = []
for _ in range(p):
    sc = list(map(int, input().split()))
    nk = list(map(int, input().split()))
    arr_sort = list(zip(sc, nk))
    arr_sort.sort(key=lambda x: x[0])
    temp = 0
    for i in range(s - 1):
        if arr_sort[i][1] > arr_sort[i + 1][1]:
            temp += 1
    a = [temp, _ + 1]
    diff.append(a)
diff = sorted(diff, key=lambda x: x[0])
for i in diff:
    print(i[1])
