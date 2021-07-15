class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        import heapq
        
        connect = list(range(N))
        def find(x):
            if connect[x]!=x:
                connect[x] = find(connect[x])
            return connect[x]
        
        def union(x, y):
            if find(x)!=find(y):
                connect[find(x)] = find(y)
        
        
        q = []
        for i in range(N):
            for j in range(i):
                w = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                q.append((w, i, j))
        q.sort()
        
        res = 0
        cnt = 0
        for w, i, j in q:
            if cnt == N-1:
                break
            if find(i) == find(j):
                continue
            else:
                res += w
                union(i, j)
                cnt += 1
        
        return res
                
        
        

