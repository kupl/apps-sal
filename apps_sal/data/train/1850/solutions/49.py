class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        root = 0
        for a, b in edges:
            dic[a].append(b)
            dic[b].append(a)

        def dfs1(curr, lvl, par):
            ret = lvl
            for nxt in dic[curr]:
                if nxt == par:
                    continue
                ret += dfs1(nxt, lvl + 1, curr)
            return ret
        from_root = dfs1(root, 0, None)
        sz = {}

        def get_sz(curr, par):
            ret = 1
            for nxt in dic[curr]:
                if nxt == par:
                    continue
                ret += get_sz(nxt, curr)
            sz[curr] = ret
            return ret
        get_sz(root, None)
        ret = [-1] * N
        ret[root] = from_root

        def go(curr, par):
            my_dist = ret[par] - sz[curr] * 2 + sz[root]
            ret[curr] = my_dist
            for nxt in dic[curr]:
                if nxt == par:
                    continue
                go(nxt, curr)
        for nxt in dic[root]:
            go(nxt, root)
        return ret
