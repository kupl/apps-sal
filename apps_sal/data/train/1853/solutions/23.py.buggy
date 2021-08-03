class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        \"\"\"priority queue + bfs \"\"\"
        graph = defaultdict(list)
        for st, ed, w in edges:
            graph[st].append((w, ed))
            graph[ed].append((w, st))

        opt = float(\"inf\")
        ans = 0
        for i in range(n):
            cnt = self.numofNeighbor(n, graph, distanceThreshold, i)            
            if cnt <= opt:
                ans, opt = i, cnt
        return ans

    def numofNeighbor(self, n, graph, distancTreshold, node):
        queue = []
        queue.append((0, node))
        visited = [False for _ in range(n)]
        cnt = 0
        while queue:
            w, v = heappop(queue)
            if visited[v]:
                continue
            cnt += 1
            visited[v] = True

            for d, neighbor in graph[v]:
                if visited[neighbor]:
                    continue
                if d + w > distancTreshold:
                    continue
                heappush(queue, (w+d, neighbor))

        return cnt
