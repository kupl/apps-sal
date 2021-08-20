class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        from heapq import heappush, heappop
        import collections
        distance = [[float('inf')] * n for _ in range(n)]
        graph = collections.defaultdict(list)
        for (i, j, w) in edges:
            distance[i][j] = distance[j][i] = w
            graph[i].append(j)
            graph[j].append(i)
        for i in range(n):
            distance[i][i] = 0
        global_min = [-1, -1]
        for i in range(n):
            count = 0
            visited = set()
            q = [(0, i)]
            while q:
                (dis, j) = heappop(q)
                if dis <= distanceThreshold:
                    count += 1
                if (i, j) not in visited and dis < distanceThreshold:
                    visited.add((i, j))
                    for nei in graph[j]:
                        distance[i][nei] = min(distance[i][nei], dis + distance[j][nei])
                        heappush(q, (distance[i][nei], nei))
        global_min = [-1, -1]
        for i in range(n):
            count = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    count += 1
            if global_min[0] == -1 or count <= global_min[0]:
                global_min[0] = count
                global_min[1] = i
        return global_min[1]
