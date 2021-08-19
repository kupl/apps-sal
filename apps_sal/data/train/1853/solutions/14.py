class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #         FLOYD WARSHALL

        dist = [[float('inf') for j in range(n)] for i in range(n)]

        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        curr = 0
        res_idx = 0
        count = float('inf')

        for i in range(n):
            curr = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    curr += 1

            if curr <= count:
                count = curr
                res_idx = i

        return res_idx
