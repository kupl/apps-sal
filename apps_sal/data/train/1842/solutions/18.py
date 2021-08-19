class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        nei = collections.defaultdict(set)
        for i, j in edges:
            nei[i].add(j)
            nei[j].add(i)

        dp = collections.deque([(1, 1, 0)])  # state: leaf_id, possibility, timestamp
        visited = set()

        while dp:
            leaf, p, curr = dp.popleft()
            visited.add(leaf)

            if curr >= t:
                if leaf == target:
                    return p
                continue

            neighbors = nei[leaf] - visited
            for n in neighbors or [leaf]:
                dp += (n, p / (len(neighbors) or 1), curr + 1),
        return 0.
