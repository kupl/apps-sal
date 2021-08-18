class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        type = [set(), set(), set()]
        for t, u, v in edges:
            type[t - 1].add(tuple(sorted([u, v])))
        res = 0
        type3type1 = type[2] & type[0]
        type3type2 = type[2] & type[1]
        res += len(type3type1) + len(type3type2)
        type[0] -= type3type1
        type[1] -= type3type2
        type3 = {i: i for i in range(1, n + 1)}

        def uf(parent, i):
            if parent[i] == i:
                return i
            parent[parent[i]] = uf(parent, parent[i])
            return parent[parent[i]]
        moved = set()
        for u, v in type[2]:
            pu = uf(type3, u)
            pv = uf(type3, v)
            if pu != pv:
                type3[pu] = pv
            else:
                moved.add((u, v))
        res += len(moved)
        type[2] -= moved
        type2 = {i: i for i in range(1, n + 1)}
        for u, v in type[1] | type[2]:
            pu, pv = uf(type2, u), uf(type2, v)
            if pu != pv:
                type2[pu] = pv
            else:
                res += 1
        cnt = 0
        for i in range(1, n + 1):
            pi = uf(type2, i)
            if pi == i:
                cnt += 1
        if cnt > 1:
            return -1
        type1 = {i: i for i in range(1, n + 1)}
        for u, v in type[0] | type[2]:
            pu, pv = uf(type1, u), uf(type1, v)
            if pu != pv:
                type1[pu] = pv
            else:
                res += 1
        cnt = 0
        for i in range(1, n + 1):
            pi = uf(type1, i)
            if pi == i:
                cnt += 1
        if cnt > 1:
            return -1
        return res
