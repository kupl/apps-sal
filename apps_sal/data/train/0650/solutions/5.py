from collections import defaultdict
from operator import itemgetter
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    diz = defaultdict(lambda: [])
    for _ in range(n):
        array = list(map(int, input().split()))
        diz[array[-1]].append((array[0], array[1]))
    counter = 0
    for key in diz:
        diz[key].sort(key=itemgetter(0))
        last_ev = diz[key][0]
        counter += 1
        for i in range(1, len(diz[key])):
            if diz[key][i][1] < last_ev[1]:
                last_ev = diz[key][i]
            elif diz[key][i][0] >= last_ev[1]:
                counter += 1
                last_ev = diz[key][i]
    print(counter)
