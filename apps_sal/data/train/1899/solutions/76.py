import collections


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        seen = set()

        islands = {2: set(), 3: set()}

        def color_island(r, c, island_id):
            seen.add((r, c))
            if A[r][c] != 1:
                return

            A[r][c] = island_id
            islands[island_id].add((r, c))

            for x, y in neighbors(r, c):
                if (x, y) not in seen:
                    color_island(x, y, island_id)

        islands_found = 0
        for r in range(m):
            if islands_found == 2:
                break
            for c in range(n):
                if islands_found == 2:
                    break
                if A[r][c] == 1:
                    islands_found += 1
                    color_island(r, c, islands_found + 1)

        source = islands[2]
        target = islands[3]

        queue = collections.deque([(node, 0) for node in source])
        seen = source
        while queue:
            (r, c), d = queue.popleft()
            if (r, c) in target:
                return d - 1
            for x, y in neighbors(r, c):
                if (x, y) not in seen:
                    queue.append(((x, y), d + 1))
                    seen.add((x, y))
