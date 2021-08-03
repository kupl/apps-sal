class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], T: int) -> int:
        dis = collections.defaultdict(lambda: float(\"inf\"))
        for i in range(n):
            dis[i, i] = 0
        for i, j, w in edges:
            dis[i, j] = dis[j, i] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i, j] = min(dis[i, j], dis[i, k]+dis[k, j])
        count = [0]*n
        for i in range(n):
            for j in range(n):
                if i == j: continue
                count[i] += dis[i, j] <= T
        mincount = min(count)
        return max(i for i, c in enumerate(count) if c == mincount)
        
