class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = collections.defaultdict(list)  # 没事不要用default(dict)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1):
                x2, y2 = points[j]
                z = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, z))
                graph[j].append((i, z))

        heap = []
        visited = set()
        heapq.heappush(heap, (0, 1))
        total = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue  # prim 算法都是先检测有没有访问过，再添加到visited里面，而不是在后面的next node添加到visited中去
            visited.add(node)
            total += cost
            if len(visited) == N:
                return total
            for nxt, c in graph[node]:
                if nxt not in visited:
                    heapq.heappush(heap, (c, nxt))  # 放入到heap中的绝对是新的单边距离，而不是总距离
        return -1
