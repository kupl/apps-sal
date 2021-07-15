class DSU:
    def __init__(self, N):
        self.parent = list(range(N+1))
        self.edges = 0

    def find(self, x):
        if x != self.parent[x]:
            # 路径完全压缩
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        # 这一句非必须，只是满足此题 需要删除此条边
        if root1 == root2:
            return 1
        
        self.parent[root2] = root1
        self.edges += 1
        
        return 0


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        ans = 0
        
        A = DSU(n)
        B = DSU(n)
        
        for t, x, y in edges:
            if t != 3:
                continue
            ans += A.union(x, y)
            B.union(x, y)
        
        for t, x, y in edges:
            if t == 3:
                continue
            # print(t, x, y)
            d = A if t == 1 else B
            ans += d.union(x, y)
            
        return ans if A.edges == n - 1 and B.edges == n - 1 else -1
            

