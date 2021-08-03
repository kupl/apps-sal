class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[sys.maxsize] * n for _ in range(n)]

        for src, tar, dis in edges:
            distances[src][tar] = dis
            distances[tar][src] = dis

        for i in range(n):
            distances[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        counts = {}
        for i, each in enumerate(distances):
            counts[len([e for e in each if e <= distanceThreshold])] = i

        return counts[min(counts)]
