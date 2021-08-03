from collections import defaultdict


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = defaultdict(list)
        for x, y, w in edges:
            dist[x].append((y, w))
            dist[y].append((x, w))

        curmin_idx, curmin_val = None, None

        def dfs(idx, visited, threshold):
            if threshold < 0:
                return
            visited[idx] = threshold

            for iidx, weight in dist[idx]:
                if (threshold - weight) > visited[iidx]:
                    dfs(iidx, visited, threshold - weight)

        for i in range(n):
            visited = [-1] * n
            dfs(i, visited, distanceThreshold)
            cur_visited = sum(1 for v in visited if v >= 0)
            if curmin_val is None or cur_visited <= curmin_val:
                curmin_val = cur_visited
                curmin_idx = i

        return curmin_idx
