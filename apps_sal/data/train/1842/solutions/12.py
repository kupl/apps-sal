class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if not edges:
            return target == 1
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)

        def dfs(idx, fr, p, step):
            if step > t:
                return 0
            if idx == target:
                if step == t or (idx != 1 and len(G[idx]) == 1 or idx == 1 and not G[idx]):
                    return p
                else:
                    return 0
            if idx != 1 and len(G[idx]) == 1:
                return 0
            for nb in G[idx]:
                if nb == fr:
                    continue
                ret = dfs(nb, idx, p / ((len(G[idx]) - 1) if idx != 1 else len(G[idx])), step + 1)
                if ret:
                    return ret
            return 0
        return dfs(1, 0, 1, 0)
