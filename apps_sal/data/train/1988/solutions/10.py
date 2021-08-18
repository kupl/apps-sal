class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(lambda: set())
        for a, b in red_edges:
            red[a].add(b)

        blue = collections.defaultdict(lambda: set())
        for a, b in blue_edges:
            blue[a].add(b)

        seen = set()
        res = [float('inf') for _ in range(n)]
        lvl = 0
        q = collections.deque([[0, 0], [0, 1]])
        while q:
            for _ in range(len(q)):
                n, c = q.popleft()
                seen.add((n, c))
                res[n] = min(lvl, res[n])
                if c:
                    for ch in red[n]:
                        if (ch, 0) not in seen:
                            q.append([ch, 0])
                else:
                    for ch in blue[n]:
                        if (ch, 1) not in seen:
                            q.append([ch, 1])
            lvl += 1

        for i, n in enumerate(res):
            if n == float('inf'):
                res[i] = -1

        return res
