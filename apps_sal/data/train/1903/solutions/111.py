class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        mst = defaultdict(set)
        graph = collections.defaultdict(dict)
        visited = [False for i in range(len(points))]
        visited[0] = True
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                graph[i][j] = (self.getDist(points[i][0], points[i][1], points[j][0], points[j][1]))
        edges = [(cost, 0, to) for to, cost in graph[0].items()]
        heapq.heapify(edges)
        while edges:
            cost, frm, to = heapq.heappop(edges)
            if not visited[to]:
                visited[to] = True
                total += cost
                for to_next, cost_next in graph[to].items():
                    if not visited[to_next]:
                        heapq.heappush(edges, (cost_next, to, to_next))
        return total
                
                
    def getDist(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
