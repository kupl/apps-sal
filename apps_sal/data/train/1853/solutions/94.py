class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def BFS(queue):
            while queue:
                route, wt = queue.popleft()
                for node, node_wt in d[route]:
                    if min_wt[node] > node_wt + wt:
                        queue.append([node, node_wt + wt])
                        min_wt[node] = node_wt + wt
            return min_wt
        d, seen, ans, m = defaultdict(list), set(), [], inf
        for x, y, z in edges:
            d[x] += [[y, z]]
            d[y] += [[x, z]]
        for i in range(n):
            min_wt = [inf] * (n)
            ans.append(BFS(deque([[i, 0]])))
            min_wt[i] = inf
        res = 0
        for q, i in enumerate(ans):
            count = 0
            for j in i:
                if j <= distanceThreshold:
                    count += 1
            if count <= m:
                res = q
                m = count
        return res
