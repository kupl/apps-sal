class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n+1)]
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1

        ans = e1 = e2 = 0
        for t, i, j in edges:
            if t == 3:
                if uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    ans += 1

        root_origin = root
        root = root_origin[:]
        for t, i , j in edges:
            if t == 1:
                if uni(i, j):
                    e1 += 1
                else:
                    ans += 1
        
        root = root_origin[:]
        for t, i, j in edges:
            if t == 2:
                if uni(i, j):
                    e2 += 1
                else:
                    ans += 1

        if e1 == n -1 and e2 == n -1:
            return ans
        else:
            return -1
