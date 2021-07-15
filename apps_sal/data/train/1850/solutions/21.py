class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # build graph as adj_list
        adj_list = defaultdict(list)
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        root = 0

        subT_size = [0]*N
        def postorder(t, par_t)->int:
            ans = 0
            for c in adj_list[t] :
                if c == par_t: continue
                ans += postorder(c, t) + subT_size[c]
                subT_size[t] += subT_size[c]
            subT_size[t] += 1
            return ans

        res = [0]*N
        def preorder(t, par_t):
            for c in adj_list[t]:
                if c == par_t: continue
                res[c] = res[t] - subT_size[c] * 2 + tot
                preorder(c, t)

        # main  
        res[root] = postorder(root, -1)
        tot = subT_size[root]
        preorder(root, -1)

        return res
