class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], D: int) -> int:
        # floyd alg to generate all pairs shortest dists
        dists = [[inf for _ in range(n)] for _ in range(n)]

        for a, b, w in edges:
            dists[a][b] = dists[b][a] = w

        for i in range(n):
            dists[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dists[i][k] + dists[k][j] < dists[i][j]:
                        dists[i][j] = dists[j][i] = dists[i][k] + dists[k][j]

        # print(dists)

        # loop through each node to find all feasible neighbours
        return min(list(range(n)), key=lambda i: (sum(int(d <= D) for d in dists[i]), -i))
