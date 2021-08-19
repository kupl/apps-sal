class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for i in range(n)]
        res = [0 for i in range(n)]
        ans = float('inf')
        city = -1
        for i in edges:
            (a, b, c) = i
            adj[a].append((b, c))
            adj[b].append((a, c))
        for i in range(n):
            visited = [float('inf') for j in range(n)]
            visited[i] = 0
            traverse(i, visited, distanceThreshold, 0, adj)
            res[i] = n - visited.count(float('inf'))
        for i in range(n):
            if res[i] <= ans:
                ans = res[i]
                city = i
        return city


def traverse(curr, visited, threshold, dist, adj):
    if dist > threshold:
        return
    visited[curr] = dist
    for pair in adj[curr]:
        (city, next_dist) = pair
        if dist + next_dist <= visited[city]:
            traverse(city, visited, threshold, dist + next_dist, adj)
