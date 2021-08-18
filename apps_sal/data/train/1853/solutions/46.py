class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mark = [[float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            mark[i][i] = 0
        for i, j, w in edges:
            mark[i][j] = w
            mark[j][i] = w
        for node in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        mark[i][j] = min(mark[i][j], mark[i][node] + mark[node][j])
        cnt = n
        ans = -1
        for i in range(n):
            cur = 0
            for j in range(n):
                if i != j and mark[i][j] <= distanceThreshold:
                    cur += 1
            if cur <= cnt:
                cnt = cur
                ans = i
        return ans
