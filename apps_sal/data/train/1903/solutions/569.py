class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        G = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                G[i].append((dis, j))
                G[j].append((dis, i))
        visited = {0}
        pq = G[0]
        heapq.heapify(pq)
        res = 0
        while len(visited) < len(points) and pq:
            (w, v) = heapq.heappop(pq)
            if v not in visited:
                res += w
                visited.add(v)
                for (w, nei) in G[v]:
                    if nei not in visited:
                        heapq.heappush(pq, (w, nei))
        return res
