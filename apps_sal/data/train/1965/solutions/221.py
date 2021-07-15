class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        for vertex
            if has type3 edge remove all other edges
            else:
                 
        '''
        dsuA = DSU(n+1)
        dsuB = DSU(n+1)
        
        ans = 0
        for t, u, v in edges:
            if t == 3:
                if not dsuA.union(u, v):
                    ans += 1
                dsuB.union(u, v)
        for t, u, v in edges:
            if t == 1:
                if not dsuA.union(u, v):
                    ans += 1
            if t == 2:
                if not dsuB.union(u, v):
                    ans += 1
        return ans if dsuA.size(1) == dsuB.size(1) == n else -1
#         hasType3 = [False for _ in range(n)]
#         graph = collections.defaultdict(list)
#         count = 0
#         for a, b, c in edges:
#             if a == 3:
#                 hasType3[b-1] = True
#                 hasType3[c-1] = True
#             graph[b].append([c, a])
#             graph[c].append([b, a])
#         seenA = [False for i in range(n)]
#         seenB = [False for i in range(n)]
#         def dfs(node, ty):
#             for nei, t in graph[node]:
#                 if ty == 1:
#                     if (t == 1 or t == 3) and not seenA[nei-1]:
#                         seenA[nei-1] = True
#                         dfs(nei, ty)
#                 if ty == 2:
#                     if (t == 2 or t == 3) and not seenB[nei-1]:
#                         seenB[nei-1] = True
#                         dfs(nei, ty)
#         dfs(edges[0][1], 1)
#         dfs(edges[0][1], 2)
#         seenA[edges[0][1]-1] = True
#         seenB[edges[0][1]-1] = True
#         # print(seenA, seenB)
#         if not all(seenA) or not all(seenB):
#             return -1
#         ans = 0
#         for i, a in enumerate(hasType3):
#             if not a:
#                 ans += 2
#             else:
#                 ans += 1

#         return max(len(edges) - ans+1, 0)

