class Solution:
    def findTheCity(self, n, edges, threshold):
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((w,v))
            adj[v].append((w,u))

        ans=0
        min_cities=100
        for x in range(n):
            cur_cities=0
            vis={x}
            dist=[threshold+1]*n
            hp=[(0,x)]
            while hp:
                d,u=heappop(hp)
                for w,v in adj[u]:
                    if d+w<=threshold and d+w<dist[v]:
                        dist[v]=d+w
                        vis.add(v)
                        heappush(hp,(d+w,v))
            if len(vis)<=min_cities:
                min_cities=len(vis)
                ans=x
        
        return ans
