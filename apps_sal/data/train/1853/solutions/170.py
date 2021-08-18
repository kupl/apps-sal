

def floydWarshall(adj, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                stopOver = adj[i][k] + adj[k][j]
                if(stopOver < adj[i][j]):
                    adj[i][j] = stopOver


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INFI = 2 ** 31
        adj = [[INFI for _ in range(n)] for _ in range(n)]
        answer = 0
        neighbors = []
        for x in range(n):
            adj[x][x] = 0

        for edge in edges:
            adj[edge[0]][edge[1]] = edge[2]
            adj[edge[1]][edge[0]] = edge[2]
        floydWarshall(adj, n)
        for node in adj:
            count = 0
            for distance in node:
                if distance <= distanceThreshold:
                    count += 1
            neighbors.append(count - 1)

        minCount = min(neighbors)
        for i, neighCount in enumerate(neighbors):
            if(minCount == neighCount):
                answer = i

        return answer
