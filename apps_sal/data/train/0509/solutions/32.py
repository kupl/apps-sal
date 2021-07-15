import sys
input = sys.stdin.readline
from collections import defaultdict, deque
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

class UnionFind(object):
	def __init__(self, N):
		self.par = [i for i in range(N)]
		self.rank = [0] * N

	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]

	def same_check(self, x, y):
		return self.find(x) == self.find(y)

	def union(self, x, y):
		x = self.find(x); y = self.find(y)
		if self.rank[x] < self.rank[y]:
			self.par[x] = y
		else:
			self.par[y] = x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1

class Graph(object):
	def __init__(self, N):
		self.graph = [[] for i in range(N)]

	def add_edge(self, a, b, c):
		self.graph[a].append((b, c))

def bfs(G, s, N):
	Q = deque(); Q.append(s)
	visit = [0] * N; visit[s] = 1
	label = [None] * N; label[s] = 0
	while Q:
		v = Q.popleft()
		for i, c in G.graph[v]:
			if visit[i] == 0:
				visit[i] = 1
				if c != label[v]:
					label[i] = c
				else:
					if c == N - 1:
						label[i] = 0
					else:
						label[i] = N - 1
				Q.append(i)
	return label

def main():
	N, M = getlist()
	G = Graph(N)
	UF = UnionFind(N)
	for i in range(M):
		u, v, c = getlist()
		u -= 1; v -= 1; c -= 1
		if UF.same_check(u, v) == False:
			UF.union(u, v)
			G.add_edge(u, v, c)
			G.add_edge(v, u, c)

	ans = bfs(G, 0, N)
	for i in ans:
		print(i + 1)


def __starting_point():
	main()
__starting_point()
