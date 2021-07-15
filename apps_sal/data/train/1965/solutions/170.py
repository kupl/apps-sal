class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def dfs(s, mp):
            for n in mp[s]:
                if visited[n] == 0:
                    visited[n] = 1
                    self.cnt += 1
                    dfs(n, mp)

        c = [0] * 4
        mpa = defaultdict(set)
        mpb = defaultdict(set)
        mpc = defaultdict(set)
        for e0, e1, e2 in edges:
            c[e0] += 1
            if e0 == 1 or e0 == 3:
                mpa[e1].add(e2)
                mpa[e2].add(e1)
            if e0 == 2 or e0 == 3:
                mpb[e1].add(e2)
                mpb[e2].add(e1)
            if e0 == 3:
                mpc[e1].add(e2)
                mpc[e2].add(e1)
                
        self.cnt = 1
        visited = [0] * (n + 1)
        visited[1] = 1
        dfs(1, mpa)
        if self.cnt != n:
            return -1

        self.cnt = 1
        visited = [0] * (n + 1)
        visited[1] = 1
        dfs(1, mpb)
        if self.cnt != n:
            return -1
        
        uc = 0
        visited = [0] * (n + 1)
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                self.cnt = 0
                dfs(i, mpc)
                uc += self.cnt
        return (c[3] - uc) + (c[1] + uc - (n-1)) + (c[2] + uc - (n-1))     

