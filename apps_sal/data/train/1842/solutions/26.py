class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        G = collections.defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        seen = set()

        def probability(idx, t):
            if t == 0:
                return idx == target
            if idx != 1 and len(G[idx]) == 1:
                return idx == target
            seen.add(idx)
            res = sum(
                probability(j, t - 1)
                for j in G[idx]
                if not j in seen
            )
            return res * 1.0 / (len(G[idx]) - (idx != 1))

        return probability(1, t)
