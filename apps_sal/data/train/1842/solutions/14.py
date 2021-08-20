from collections import defaultdict, deque


class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        nei = collections.defaultdict(set)
        for (a, b) in edges:
            nei[a].add(b)
            nei[b].add(a)
        dp = collections.deque([(1, 1, 0)])
        visited = set()
        while dp:
            (leaf, p, curr) = dp.popleft()
            visited.add(leaf)
            if curr >= t:
                if leaf == target:
                    return p
                continue
            neighbors = nei[leaf] - visited
            for n in neighbors or [leaf]:
                dp += ((n, p / (len(neighbors) or 1), curr + 1),)
        return 0.0
