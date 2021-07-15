class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        temp = [[], [], []]
        for t, a, b in edges:
            temp[t - 1].append([a, b])
                
        p = list(range(n + 1))
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        def union(i, j):
            p[find(i)] = find(j)
        
        def helper(c):
            ans = 0
            for x, y in c:
                if find(x) == find(y):
                    ans += 1
                else:
                    union(x, y)
            return ans

        res = helper(temp[2])
        old = p[:]
        for c in temp[:2]:
            res += helper(c)
            p = old
        if sum(x == p[x] for x in range(1, n + 1)) == 1:
            return res
        return -1
        
        



