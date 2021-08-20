class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for (v1, v2) in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        root = 0
        subT_size = {}

        def postorder(t, par_t) -> int:
            if len([c for c in adj_list[t] if c != par_t]) == 0:
                subT_size[t] = 1
                return 0
            else:
                ans = sum((postorder(c, t) for c in adj_list[t] if c != par_t))
                subT_size[t] = sum((subT_size[c] for c in adj_list[t] if c != par_t)) + 1
                return ans + subT_size[t] - 1
        res = [0] * N

        def preorder(t, par_t):
            res[t] = res[par_t] - subT_size[t] * 2 + tot
            for c in adj_list[t]:
                if c != par_t:
                    preorder(c, t)
        res[root] = postorder(root, -1)
        tot = subT_size[root]
        print(subT_size)
        for c in adj_list[root]:
            preorder(c, root)
        return res
