import scipy.sparse
from itertools import product
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


xs, ys, xt, yt = list(map(int, input().split()))
n = int(input())
xyr = [None] * (n + 2)
for i in range(n):
    xyr[i] = tuple(map(int, input().split()))
# ns = [[] for _ in range(n+2)]
data = []
rs = []
cs = []
s = n
t = n + 1
xyr[s] = (xs, ys, 0)
xyr[t] = (xt, yt, 0)
for i, j in product(range(n + 2), range(n + 2)):
    if i < j:
        d = max(0, ((xyr[i][0] - xyr[j][0])**2 + (xyr[i][1] - xyr[j][1])**2)**0.5 - (xyr[i][2] + xyr[j][2]))
        data.append(d)
        rs.append(i)
        cs.append(j)
m = scipy.sparse.csr_matrix((data, (rs, cs)), shape=(n + 2, n + 2))
ans = scipy.sparse.csgraph.dijkstra(m, indices=t, directed=False)
print(ans[s])
