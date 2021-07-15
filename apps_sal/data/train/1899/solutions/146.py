class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:     
        def neighbors(u, v):
            for du, dv in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nu, nv = u + du, v + dv
                if 0<=nu<m and 0<=nv<n:
                    yield (nu, nv)
        def components():
            def dfs(u, v, acc):
                acc.add((u, v))
                visited.add((u, v))
                
                for nu,nv in neighbors(u, v):
                    if (nu,nv) not in visited and A[nu][nv] == 1:
                        dfs(nu,nv,acc)
            res = []
            visited = set()
            for u in range(m):
                for v in range(n):
                    if A[u][v] == 1 and (u,v) not in visited:
                        res.append(set())
                        dfs(u,v, res[-1])
            return res
        def bfs(ps, pt):
            q = deque()
            visited = set()
            for p in ps:
                q.append(p)
                visited.add(p)
            distance = 0
            while q:
                qsize = len(q)
                for i in range(qsize):
                    (u, v) = q.popleft()
                    for nu, nv in neighbors(u, v):
                        if (nu,nv) in pt:
                            return distance
                        if (nu, nv) not in visited:
                            q.append((nu, nv))
                            visited.add((nu, nv))
                distance += 1
            return 0
                    
                
        
        m = len(A)
        n = len(A[0])
        
        source, target = components()
        print(source)
        print(target)
        
        return bfs(source, target)

