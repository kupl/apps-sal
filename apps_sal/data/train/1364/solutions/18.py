#from statistics import median
from collections import defaultdict

T = int(input().rstrip())
for tt in range(T):
    N, c = list(map(int, input().rstrip().split(" ")))

    hh = defaultdict(list)
    for i in range(N):
        x, y = list(map(int, input().rstrip().split(" ")))
        hh[(x - y, ((x % c) + c) % c)].append(x)

    # print(hh)
    opr = 0

    for j in hh:

        arr = hh[j]
        # print(arr)
        arr.sort()
        med = arr[len(arr) // 2]
        tp = 0
        for k in arr:
            tp += abs(med - k) // c

        opr += tp

    print(len(hh), int(opr))
