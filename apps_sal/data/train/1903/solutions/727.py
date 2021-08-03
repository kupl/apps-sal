class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        dist = []

        for x in range(len(points)):
            [xi, yi] = points[x]
            for y in range(x + 1, len(points)):
                [xj, yj] = points[y]
                manhattan_dist = abs(xi - xj) + abs(yi - yj)
                if x != y:
                    dist.append([x, y, manhattan_dist])

        dist.sort(key=lambda pt: pt[2])

        def detectCycle(adj):
            visited = set()

            def dfs(curr, parent):
                visited.add(curr)
                for neighbor in adj[curr]:
                    if neighbor == parent:
                        continue
                    elif neighbor in visited:
                        return True
                    elif dfs(neighbor, curr):
                        return True
                return False

            for node in range(len(points)):
                if node not in visited:
                    if dfs(node, -1):
                        return True
            return False

        adj = {x: set() for x in range(len(points))}
        ans = 0
        v = 0
        for distance in dist:
            [x, y, manhattan_dist] = distance
            adj[x].add(y)
            adj[y].add(x)
            if detectCycle(adj):
                adj[x].remove(y)
                adj[y].remove(x)
            else:
                ans += manhattan_dist
                v += 1

            if v == len(points) - 1:
                break

        return ans
