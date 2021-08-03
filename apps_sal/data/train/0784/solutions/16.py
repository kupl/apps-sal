from sys import stdout, stdin
from operator import itemgetter
n, m, p = list(map(int, stdin.readline().split()[0:3]))
increases = {}
for _ in range(p):
    i, j = list(map(int, stdin.readline().split()[0:2]))
    if not i in increases:
        increases[i] = {}
        increases[i][j] = 1
    else:
        if j in increases[i]:
            increases[i][j] += 1
        else:
            increases[i][j] = 1
for row in range(1, n + 1, 1):
    base = m - 1
    if not row in increases or m == 1:
        print(base)
    else:
        keylist = list(increases[row].keys())
        keylist.sort()
        for key in keylist:
            if key == m:
                base += increases[row][key]
                continue
            if not key + 1 in increases[row]:
                if increases[row][key] >= 2:
                    base = -1
                    break
                if key == 1:
                    base -= increases[row][key]
                    continue
            else:
                if increases[row][key] - increases[row][key + 1] >= 2:
                    base = -1
                    break
                else:
                    if key == 1:
                        base -= increases[row][key]
                    continue
        print(base)
