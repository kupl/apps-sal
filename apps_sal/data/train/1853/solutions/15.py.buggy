class Solution:
    def findTheCity(self, n, edges, maxd):
        \"\"\"
        * dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        # res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        \"\"\"
        
        \"\"\"
        城市i到城市j的距離矩陣:
        [[0, 2, 5, 5, 4], 
         [2, 0, 3, 3, 2], 
         [5, 3, 0, 1, 2], 
         [5, 3, 1, 0, 1], 
         [4, 2, 2, 1, 0]]
        \"\"\"
        dis = [[float('inf')] * n for _ in range(n)] # 城市i到城市j的距離矩陣
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        
        for i in range(n):
            dis[i][i] = 0
        
        # ### wrong!
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)} # {數目: 城市}
        return res[min(res)]
