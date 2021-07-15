class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        for t,x,y in e:
            g[x-1].append((y-1,t))
            g[y-1].append((x-1,t))

        def sub(f):
            res=[0]
            s=[0]
            def dfs(now,q):
                if 1<<now&s[0]:return 
                s[0]|=1<<now
                if q:
                    res[0]+=1
                for nex,t in g[now]:
                    if t==f or t==3:
                        dfs(nex,0)
            for i in range(n):
                dfs(i,1)
            return res[0]

        if sub(1)>1 or sub(2)>1:
            return -1
        return len(e)-(n-2+sub(3))

