class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float(inf)] * n for _ in range(n)]
        for (i, j, w) in edges:
            dis[i][j] = w
            dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum((d <= distanceThreshold for d in dis[i])): i for i in range(n)}
        print(res)
        return res[min(res)]
        ' dfs not working, https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490555/The-Reason-of-DFS-Not-Working-(Explain-Graph-and-Example)\n        d = collections.defaultdict(list)\n        lookup = dict({})\n        for e in edges:\n            s, e, l = e[0], e[1], e[2]\n            d[s].append(e)\n            d[e].append(s)\n            lookup[(s,e)]=l\n            lookup[(e,s)]=l\n        \n        res=collections.defaultdict(list)\n        def dfs(j: int, i:int, t:int, v:set):\n\n            for c in d[i]:\n                if c not in v and c != j and lookup[(i,c)] <= t:\n                    res[j].append(c)\n                    v.add(c)\n                    dfs(j, c, t-lookup[i,c], v)\n                \n        \n        for i in range(n):\n            dfs(i, i, distanceThreshold, set({}))\n        if n > 26:\n            print("27={},33={}".format(res[27], res[33]))\n        mm = len(res[0])\n        r = 0\n        for i in range(n):\n            print("{},len:{}".format(i, len(res[i])))\n            if len(res[i])  <= mm:\n                r = i\n                mm = len(res[i])\n        return r\n        '
