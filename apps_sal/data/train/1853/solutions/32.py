class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for (i, j, w) in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        print(dis)
        ans = 0
        mmin = n
        for i in range(n):
            count = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    count += 1
            if count <= mmin:
                mmin = count
                ans = i
        return ans
