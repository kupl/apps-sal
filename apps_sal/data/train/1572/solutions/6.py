from multiprocessing import SimpleQueue as queue
from collections import defaultdict
from operator import itemgetter


def visit(v, i):
    height[v][1] = i
    for u in sons[v]:
        visit(u, i + 1)
    return


inp = list(map(int, input().split()))
n = inp[0]
wealth = inp[1:n + 1]
father = [i - 1 if i > 0 else i for i in inp[n + 1:]]
sons = defaultdict(lambda: [])
for i in range(n):
    if father[i] != -1:
        sons[father[i]].append(i)
    else:
        boss = i
height = [[i, 0] for i in range(n)]
visit(boss, 0)
height.sort(key=itemgetter(1), reverse=True)
minimi = [0] * n
diff = [0] * n
for el in height:
    v = el[0]
    if len(sons[v]) == 0:
        minimi[v] = wealth[v]
        diff[v] = -float('Inf')
    else:
        minimo = min([minimi[u] for u in sons[v]])
        minimi[v] = min(minimo, wealth[v])
        diff[v] = max(max([diff[u] for u in sons[v]]), wealth[v] - minimo)
print(diff[boss])
'\ncoda=queue()\nfor i in range(n):\n    if len(sons[i])==0:\n        coda.put(i)\n        visited[i]=1\nwhile len(coda)>0:\n    '
