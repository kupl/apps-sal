class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        from heapq import heappush, heappop
        import collections
        distance = [[float('inf')] * n for _ in range(n)]
        graph = collections.defaultdict(list);
        # initialize the graph and distance matrix
        for i, j, w in edges:
            distance[i][j] = distance[j][i] = w
            graph[i].append(j)
            graph[j].append(i)
        for i in range(n):
            distance[i][i] = 0
        
        # use dijkstra algorithm for every node
        global_min = [-1, -1]
        for i in range(n):
            count = set()
            visited = set()
            q = [(0, i)]
            while q:
                dis, j = heappop(q)
                if dis <= distanceThreshold:
                    count.add(j)
                if (i, j) not in visited and dis < distanceThreshold:
                    visited.add((i, j))
                    for nei in graph[j]:
                        distance[i][nei] = min(distance[i][nei], dis + distance[j][nei])
                        heappush(q, (distance[i][nei], nei))
            # print(count)
            if global_min[0] == -1 or len(count) <= global_min[0]:
                global_min[0] = len(count)
                global_min[1] = i
        
        return global_min[1]

