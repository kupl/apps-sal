import sys
from bisect import bisect_left
def input():
	return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**6)

n = int(input())
d = [[int(input()), i+1] for i in range(n)]
check = d[0][0]
d.sort()
ind = [x[1] for x in d]
d = [x[0] for x in d]
if n <= 3:
	print(-1)
	return
#print(d)
child = [1 for _ in range(n)]
#print(gap)
ans = []
adj = [[] for _ in range(n)]
for i in range(n-1, 0, -1):
	x = d[i]
	b = bisect_left(d, x - n + 2*child[i])
	#print(i, x, n - 2+child[i], b)
	if d[b] != x - n + 2*child[i] or n <= 2*child[i]:
		print(-1)
		return
	else:
		child[b] += child[i]
		ans.append([ind[b], ind[i]])
		adj[ind[b]-1].append(ind[i]-1)
		adj[ind[i]-1].append(ind[b]-1)


res = 0
def dfs(x, p, dis):
	nonlocal res
	res += dis
	for v in adj[x]:
		if v == p:
			continue
		else:
			dfs(v, x, dis+1)
	return

dfs(0, -1, 0)
if res == check:
	for a in ans:
		print(*a)
else:
	print(-1)
