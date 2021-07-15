import sys
from collections import deque
def input():
	return sys.stdin.readline()[:-1]

INF = 10**6
t = int(input())
for _ in range(t):
	n, m, a, b, c = map(int, input().split())
	a, b, c = a-1, b-1, c-1
	p = list(map(int, input().split()))
	p.sort()
	cum = [0 for _ in range(m+1)]
	for i, x in enumerate(p):
		cum[i+1] = cum[i] + x
	adj = [[] for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())
		adj[u-1].append(v-1)
		adj[v-1].append(u-1)

	a_dist, b_dist, c_dist = [INF for _ in range(n)], [INF for _ in range(n)], [INF for _ in range(n)]

	a_dist[a] = 0
	q = deque([a])
	while q:
		l = q.popleft()
		for v in adj[l]:
			if a_dist[v] > a_dist[l]+1:
				a_dist[v] = a_dist[l]+1
				q.append(v)

	b_dist[b] = 0
	q = deque([b])
	while q:
		l = q.popleft()
		for v in adj[l]:
			if b_dist[v] > b_dist[l]+1:
				b_dist[v] = b_dist[l]+1
				q.append(v)

	c_dist[c] = 0
	q = deque([c])
	while q:
		l = q.popleft()
		for v in adj[l]:
			if c_dist[v] > c_dist[l]+1:
				c_dist[v] = c_dist[l]+1
				q.append(v)
	
	#print(a_dist)
	#print(b_dist)
	#print(c_dist)
	ans = 10**20
	for i in range(n):
		aa, bb, cc = a_dist[i], b_dist[i], c_dist[i]
		#print(aa, bb, cc)
		if aa+bb+cc > m:
			continue
		ans = min(ans, cum[aa+bb+cc] + cum[bb])
	print(ans)
