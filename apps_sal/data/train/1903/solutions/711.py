import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.maxRank = 1

    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
            self.maxRank = max(self.maxRank, self.rank[pa])
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
            self.maxRank = max(self.maxRank, self.rank[pb])

    # find the representative of the
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(u, v):
            dx = abs(u[0] - v[0])
            dy = abs(u[1] - v[1])
            return dx + dy

        n = len(points)
        if n == 1:
            return 0
        if n == 2:
            return distance(points[0], points[1])

        # # Method 1: Prim's Alg with Heap
        # d = {i:[] for i in range(n)}
        # for i in range(n):
        #     for j in range(i+1, n):
        #         dist = distance(points[i], points[j])
        #         d[i].append((dist, j))
        #         d[j].append((dist, i))
        # cost = 0
        # connected = 1
        # check = [True] + [False]*(n-1)
        # heap = d[0]
        # heapq.heapify(heap)
        # while connected < n:
        #     (dist, p) = heapq.heappop(heap)
        #     if not check[p]:
        #         cost += dist
        #         connected += 1
        #         check[p] = True
        #         for pair in d[p]:
        #             heapq.heappush(heap, pair)
        # return cost

        # # Nethod 2: Another Implementation of Prim's Alg
        # cost = 0
        # curr = 0 # select a random point as the starting point
        # dist = [float('inf')] * n
        # explored = set()
        # explored.add(0)
        # cnt = 1
        # while cnt < n:
        #     u = points[curr]
        #     for j, v in enumerate(points):
        #         if j in explored:
        #             continue
        #         else:
        #             dist[j] = min(dist[j], distance(u,v))
        #     min_d, curr = min((d, j) for j, d in enumerate(dist))
        #     explored.add(curr)
        #     cnt += 1
        #     dist[curr] = float('inf')
        #     cost += min_d
        # return cost

        # Method 3: Kruskal's Alg with Disjoint Set
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(points[i], points[j])
                edges.append((dist, i, j))
        heapq.heapify(edges)
        cost = 0
        ds = DisjointSet(n)
        while ds.maxRank < n:
            dist, u, v = heapq.heappop(edges)
            if ds.find(u) != ds.find(v):
                cost += dist
                ds.union(u, v)
        return cost
