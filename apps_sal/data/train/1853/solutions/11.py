class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float(inf)] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = w
            dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        print(res)
        return res[min(res)]

        ''' dfs not working, https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490555/The-Reason-of-DFS-Not-Working-(Explain-Graph-and-Example)
        d = collections.defaultdict(list)
        lookup = dict({})
        for e in edges:
            s, e, l = e[0], e[1], e[2]
            d[s].append(e)
            d[e].append(s)
            lookup[(s,e)]=l
            lookup[(e,s)]=l
        
        res=collections.defaultdict(list)
        def dfs(j: int, i:int, t:int, v:set):

            for c in d[i]:
                if c not in v and c != j and lookup[(i,c)] <= t:
                    res[j].append(c)
                    v.add(c)
                    dfs(j, c, t-lookup[i,c], v)
                
        
        for i in range(n):
            dfs(i, i, distanceThreshold, set({}))
        if n > 26:
            print(\"27={},33={}\".format(res[27], res[33]))
        mm = len(res[0])
        r = 0
        for i in range(n):
            print(\"{},len:{}\".format(i, len(res[i])))
            if len(res[i])  <= mm:
                r = i
                mm = len(res[i])
        return r
        '''
