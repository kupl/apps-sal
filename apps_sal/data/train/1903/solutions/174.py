import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            dx = abs(x[0] - y[0])
            dy = abs(x[1] - y[1])
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
        #         check[p] = 1
        #         for pair in d[p]:
        #             heapq.heappush(heap, pair)
        # return cost

        # Method 2: Kruskal's Alg with Disjoint Set

        # Nethod 3: Greedy
        cost = 0
        curr = 0  # select a random point as the starting point
        dist = [float('inf')] * n
        explored = set()
        explored.add(0)
        cnt = 1
        while cnt < n:
            x = points[curr]
            for j, y in enumerate(points):
                if j in explored:
                    continue
                else:
                    dist[j] = min(dist[j], distance(x, y))
            min_d, curr = min((d, j) for j, d in enumerate(dist))
            explored.add(curr)
            cnt += 1
            dist[curr] = float('inf')
            cost += min_d
        return cost
