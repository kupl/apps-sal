class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        def get_root(i):
            if parents[i] == i:
                return i
            root = get_root(parents[i])
            parents[i] = root
            return root

        def join(i, j):
            root = get_root(i)
            parents[root] = j

        parents = [_ for _ in range(len(points))]
        Q = []

        for i, p in enumerate(points):
            for j, q in enumerate(points):
                if i >= j:
                    continue
                heapq.heappush(Q, (distance(p, q), i, j))

        answer = 0
        while Q:
            d, i, j = heapq.heappop(Q)
            if get_root(i) == get_root(j):
                continue
            else:
                join(i, j)
                answer += d
        return answer
