import sys
(n, m) = list(map(int, input().split()))
k = 0
pos = 0
L = []
L1 = []
d = {i: [0, -1] for i in range(1, n + 1)}
for i in range(m):
    (a, b) = list(map(int, sys.stdin.readline()[:-1].split()))
    if a == 1:
        d[b][0] += 1
        k += 1
        L.append(b)
    elif a == 2:
        k -= d[b][0]
        d[b][0] = 0
        d[b][1] = len(L)
    else:
        for j in range(pos, b):
            if d[L[j]][0] > 0 and d[L[j]][1] < j + 1:
                k -= 1
                d[L[j]][0] -= 1
        pos = max(pos, b)
    L1.append(k)
sys.stdout.write('\n'.join(map(str, L1)))
