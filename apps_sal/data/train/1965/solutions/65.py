class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]], check_type=1) -> int:
        mem = {i: i for i in range(1, n + 1)}

        def find(k):
            if mem[k] != k:
                mem[k] = find(mem[k])
            return mem[k]

        def union(k1, k2):
            (f1, f2) = (find(k1), find(k2))
            if f1 != f2:
                mem[f1] = f2
        res = 0
        for (t, e1, e2) in edges:
            if t == 3:
                (f1, f2) = (find(e1), find(e2))
                if f1 == f2 and check_type == 1:
                    res += 1
                union(e1, e2)
        for (t, e1, e2) in edges:
            if t == check_type:
                (f1, f2) = (find(e1), find(e2))
                if f1 == f2:
                    res += 1
                else:
                    union(f1, f2)
        roots = set(map(find, list(range(1, n + 1))))
        if len(roots) > 1:
            return -1
        if check_type == 1:
            res2 = self.maxNumEdgesToRemove(n, edges, check_type=2)
            if res2 == -1:
                return -1
            return res + res2
        else:
            return res
