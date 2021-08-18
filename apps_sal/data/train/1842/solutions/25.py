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
            res, count = 0, 0
            for j in G[idx]:
                if not j in seen:
                    res += probability(j, t - 1)
                    count += 1
            return res / count

        return probability(1, t)
